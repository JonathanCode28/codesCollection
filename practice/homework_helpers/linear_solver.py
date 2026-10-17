"""
Step-by-Step Linear Equation & Inequality Solver
=================================================

Solves linear equations and inequalities in one variable (x) -- '=', '<',
'>', '<=', '>=' -- and prints the line after every algebraic operation:
opening brackets, gathering like terms, moving variable terms across the
sign, moving constants across the sign, and finally isolating x.

Design notes (why it's built this way, not with eval()/sympy.solve()):
  - No eval(): user input is never executed as Python code -- it is
    tokenized and parsed into a small expression tree, so malformed or
    malicious input just raises a clear ValueError instead of running
    arbitrary code.
  - No sympy.solve(): sympy auto-combines like terms the instant an
    expression is built, so you can't stop it mid-way to show "opened
    brackets, not yet combined". Full manual control was needed instead.
  - fractions.Fraction is used for every computation, so results are
    always exact (2/3 stays 2/3, never 0.6666666666666666).
  - Tokenizing, parsing and expanding are each a single linear (O(n))
    pass over the input -- no re-parsing, no repeated string scanning.
  - Pure Python, no C extension: the entire input (a short arithmetic
    string) is parsed and solved in well under a millisecond, so there is
    no realistic input size here where a C rewrite would be measurably
    faster. The complexity that would matter -- manual malloc/free,
    buffer handling, no built-in exact-fraction type -- would be added
    for no real gain.

Supports:
    - x on one side or both sides of the equation/inequality
    - all five comparators: =, <, >, <=, >=
    - the sign-flip rule when multiplying/dividing both sides by a
      negative number (shown as its own explicit step)
    - parentheses AND square brackets, including nested/mixed ('(' must
      close with ')', '[' must close with ']' -- mismatches raise a
      clear error)
    - fractions and division by a constant (e.g. "x/2 + 1/3 = 5/6",
      "(x+1)/2 = (x-1)/3"), with an explicit "find the common
      denominator and multiply every term by it" step that clears all
      fractions at once, same as doing it by hand
    - integers, decimals, negative numbers
    - implicit multiplication: "2x", "2(x+3)", "2[x+3]", "-(x-1)"
    - "no solution" / "true for every real number" cases

Usage:
    python linear_solver.py "2*(x + 3) - 4 = 5*x - 1"
    python linear_solver.py "3x - 2 <= 5x + 1"
    python linear_solver.py "(x+1)/2 = (x-1)/3"
    python linear_solver.py                  # interactive mode
"""

from __future__ import annotations

import operator as opmod
import os
import re
import sys
from fractions import Fraction
from math import gcd
from typing import List, NamedTuple, Optional, Tuple, Union

# =============================================================================
# 1. Tokenizer
# =============================================================================

_TOKEN_RE = re.compile(r"\d+\.\d+|\d+|[xX]|[+\-*/()\[\]=]|\s+")
_NUMBER_RE = re.compile(r"^\d+(\.\d+)?$")


def tokenize(text: str) -> List[str]:
    """Turn a raw string into a flat list of tokens. O(n)."""
    tokens: List[str] = []
    pos = 0
    for m in _TOKEN_RE.finditer(text):
        if m.start() != pos:
            bad = text[pos:m.start()]
            raise ValueError(f"Unexpected character(s) {bad!r} in {text!r}")
        pos = m.end()
        tok = m.group()
        if tok.isspace():
            continue
        tokens.append("x" if tok.lower() == "x" else tok)
    if pos != len(text):
        raise ValueError(f"Unexpected character(s) {text[pos:]!r} at end of {text!r}")
    return tokens


def insert_implicit_multiplication(tokens: List[str]) -> List[str]:
    """Turn '2x', '2(x+1)', '2[x+1]', ')(' etc. into an explicit '*' token. O(n)."""
    def ends_value(tok: str) -> bool:
        return tok in (")", "]") or tok == "x" or bool(_NUMBER_RE.match(tok))

    def starts_value(tok: str) -> bool:
        return tok in ("(", "[") or tok == "x" or bool(_NUMBER_RE.match(tok))

    out: List[str] = []
    for tok in tokens:
        if out and ends_value(out[-1]) and starts_value(tok):
            out.append("*")
        out.append(tok)
    return out


# =============================================================================
# 2. Expression tree + recursive-descent parser
#    grammar:  expr   := term (('+'|'-') term)*
#              term   := factor (('*'|'/') factor)*
#              factor := NUMBER | 'x' | '(' expr ')' | '[' expr ']' | '-' factor | '+' factor
# =============================================================================

class Num:
    __slots__ = ("value",)
    def __init__(self, value: Fraction) -> None:
        self.value = value


class Var:
    __slots__ = ()


class Neg:
    __slots__ = ("node",)
    def __init__(self, node: "Node") -> None:
        self.node = node


class Add:
    __slots__ = ("terms",)
    def __init__(self, terms: List[Tuple[str, "Node"]]) -> None:
        self.terms = terms  # list of (sign, node), sign is '+' or '-'


class Mul:
    __slots__ = ("factors",)
    def __init__(self, factors: List["Node"]) -> None:
        self.factors = factors


class Div:
    __slots__ = ("numerator", "denominator")
    def __init__(self, numerator: "Node", denominator: "Node") -> None:
        self.numerator = numerator
        self.denominator = denominator


Node = Union[Num, Var, Neg, Add, Mul, Div]


class Parser:
    def __init__(self, tokens: List[str]) -> None:
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> Optional[str]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self) -> str:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expect(self, tok: str) -> None:
        if self.peek() != tok:
            raise ValueError(f"Expected '{tok}' but found {self.peek()!r}")
        self.advance()

    def parse_expr(self) -> Node:
        first = self.parse_term()
        terms: List[Tuple[str, Node]] = [("+", first)]
        while self.peek() in ("+", "-"):
            op = self.advance()
            terms.append((op, self.parse_term()))
        return first if len(terms) == 1 else Add(terms)

    def parse_term(self) -> Node:
        # Left-to-right chain of '*' and '/' at equal precedence, e.g.
        # "2*x/3*5" -> ((2*x)/3)*5. Consecutive '*' factors are grouped
        # into a single Mul (used by expand() to detect x*x); each '/'
        # wraps everything accumulated so far in a Div and restarts.
        node = self.parse_factor()
        pending_mul: List[Node] = [node]
        while self.peek() in ("*", "/"):
            op = self.advance()
            rhs = self.parse_factor()
            if op == "*":
                pending_mul.append(rhs)
            else:
                base = pending_mul[0] if len(pending_mul) == 1 else Mul(pending_mul)
                pending_mul = [Div(base, rhs)]
        return pending_mul[0] if len(pending_mul) == 1 else Mul(pending_mul)

    def parse_factor(self) -> Node:
        tok = self.peek()
        if tok == "-":
            self.advance()
            return Neg(self.parse_factor())
        if tok == "+":
            self.advance()
            return self.parse_factor()
        if tok == "(":
            self.advance()
            node = self.parse_expr()
            self.expect(")")
            return node
        if tok == "[":
            self.advance()
            node = self.parse_expr()
            self.expect("]")
            return node
        if tok == "x":
            self.advance()
            return Var()
        if tok is not None and _NUMBER_RE.match(tok):
            self.advance()
            return Num(Fraction(tok))
        raise ValueError(f"Unexpected token {tok!r}")


def parse_side(text: str) -> Node:
    tokens = insert_implicit_multiplication(tokenize(text))
    if not tokens:
        raise ValueError("Empty expression.")
    parser = Parser(tokens)
    node = parser.parse_expr()
    if parser.pos != len(parser.tokens):
        raise ValueError(f"Unexpected token {parser.peek()!r} in {text!r}")
    return node


# =============================================================================
# 3. Expanding brackets -> a flat list of terms (not yet combined)
# =============================================================================

class Term(NamedTuple):
    coeff: Fraction
    is_var: bool


def expand(node: Node) -> List[Term]:
    """Distribute every Mul over Add so brackets disappear. O(n) in tree size."""
    if isinstance(node, Num):
        return [Term(node.value, False)]
    if isinstance(node, Var):
        return [Term(Fraction(1), True)]
    if isinstance(node, Neg):
        return [Term(-t.coeff, t.is_var) for t in expand(node.node)]
    if isinstance(node, Add):
        out: List[Term] = []
        for sign, sub in node.terms:
            sub_terms = expand(sub)
            if sign == "-":
                sub_terms = [Term(-t.coeff, t.is_var) for t in sub_terms]
            out.extend(sub_terms)
        return out
    if isinstance(node, Mul):
        scalar = Fraction(1)
        var_terms: Optional[List[Term]] = None
        for factor in node.factors:
            f_terms = expand(factor)
            if any(t.is_var for t in f_terms):
                if var_terms is not None:
                    raise ValueError(
                        "This is not a linear equation (it contains x^2 or a higher power)."
                    )
                var_terms = f_terms
            else:
                scalar *= sum((t.coeff for t in f_terms), Fraction(0))
        if var_terms is None:
            return [Term(scalar, False)]
        return [Term(scalar * t.coeff, t.is_var) for t in var_terms]
    if isinstance(node, Div):
        num_terms = expand(node.numerator)
        denom_terms = expand(node.denominator)
        if any(t.is_var for t in denom_terms):
            raise ValueError(
                "Dividing by an expression containing x is not supported "
                "(the equation would no longer be linear)."
            )
        denom_value = sum((t.coeff for t in denom_terms), Fraction(0))
        if denom_value == 0:
            raise ValueError("Division by zero in the equation.")
        return [Term(t.coeff / denom_value, t.is_var) for t in num_terms]
    raise TypeError(f"Unknown node type: {type(node)!r}")


def has_brackets_to_open(node: Node) -> bool:
    """True if expanding this node actually requires distributing something."""
    if isinstance(node, (Num, Var)):
        return False
    if isinstance(node, Neg):
        return isinstance(node.node, Add) or has_brackets_to_open(node.node)
    if isinstance(node, Add):
        return any(has_brackets_to_open(sub) for _, sub in node.terms)
    if isinstance(node, Mul):
        if any(isinstance(f, Add) for f in node.factors):
            return True
        return any(has_brackets_to_open(f) for f in node.factors)
    if isinstance(node, Div):
        return has_brackets_to_open(node.numerator) or has_brackets_to_open(node.denominator)
    return False


def combine(terms: List[Term]) -> Tuple[Fraction, Fraction]:
    """Sum all x-terms and all constant terms separately."""
    var_sum = sum((t.coeff for t in terms if t.is_var), Fraction(0))
    const_sum = sum((t.coeff for t in terms if not t.is_var), Fraction(0))
    return var_sum, const_sum


def needs_combining(terms: List[Term]) -> bool:
    var_count = sum(1 for t in terms if t.is_var)
    const_count = sum(1 for t in terms if not t.is_var)
    return var_count > 1 or const_count > 1


def common_denominator(*fractions: Fraction) -> int:
    """LCM of the denominators of the given Fractions. 1 means 'no fractions'."""
    lcd = 1
    for f in fractions:
        lcd = lcd * f.denominator // gcd(lcd, f.denominator)
    return lcd


# =============================================================================
# 4. Formatting helpers (build the human-readable equation strings)
# =============================================================================

def fmt_frac(f: Fraction) -> str:
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def _piece(magnitude: Fraction, is_var: bool) -> str:
    if is_var:
        if magnitude == 1:
            return "x"
        # Wrap fractional coefficients in parens: "(3/2)x", not the
        # ambiguous "3/2x" which reads like 3 / (2x).
        return f"{magnitude.numerator}x" if magnitude.denominator == 1 else f"({fmt_frac(magnitude)})x"
    return fmt_frac(magnitude)


def format_terms(terms: List[Term]) -> str:
    """Render a (possibly un-combined) list of terms, e.g. '2x + 6 - 4'."""
    if not terms:
        return "0"
    parts = []
    for i, t in enumerate(terms):
        piece = _piece(abs(t.coeff), t.is_var)
        if i == 0:
            parts.append(f"-{piece}" if t.coeff < 0 else piece)
        else:
            parts.append(f"{'-' if t.coeff < 0 else '+'} {piece}")
    return " ".join(parts)


def format_side(var_coeff: Fraction, const: Fraction) -> str:
    """Render an already-combined side, e.g. format_side(2, -3) -> '2x - 3'."""
    terms: List[Term] = []
    if var_coeff != 0:
        terms.append(Term(var_coeff, True))
    if const != 0 or not terms:
        terms.append(Term(const, False))
    return format_terms(terms)


# =============================================================================
# 5. Comparators -- '=', '<', '>', '<=', '>='
# =============================================================================

_COMPARATOR_RE = re.compile(r"<=|>=|=|<|>")

_EVAL = {"=": opmod.eq, "<": opmod.lt, ">": opmod.gt, "<=": opmod.le, ">=": opmod.ge}
_FLIP = {"=": "=", "<": ">", ">": "<", "<=": ">=", ">=": "<="}


def split_on_comparator(text: str) -> Tuple[str, str, str]:
    """Split 'left <cmp> right' into (left, cmp, right). O(n)."""
    matches = list(_COMPARATOR_RE.finditer(text))
    if not matches:
        raise ValueError("No comparison ('=', '<', '>', '<=', '>=') found.")
    if len(matches) > 1:
        raise ValueError(
            "Only one comparison per input is supported "
            "(compound inequalities like '3 < x < 7' aren't supported yet)."
        )
    m = matches[0]
    return text[:m.start()], m.group(), text[m.end():]


class Solution(NamedTuple):
    """Result of solve(). 'kind' is one of:
       'unique'     -> a single x <comparator> value
       'all_reals'  -> every real number satisfies it
       'no_solution'-> nothing satisfies it
    comparator/value are only meaningful when kind == 'unique'."""
    kind: str
    comparator: Optional[str]
    value: Optional[Fraction]


# =============================================================================
# 6. The solver itself -- orchestrates the steps and prints each one
# =============================================================================

def solve(problem: str, verbose: bool = True) -> Solution:
    """
    Solve a linear equation or inequality in x, printing every step.

    Addition/subtraction of the same quantity on both sides never changes
    a comparator's direction, so every step here is comparator-agnostic
    *except* the final division: dividing both sides by a negative number
    flips '<' <-> '>' and '<=' <-> '>=' ('=' is never affected).
    """
    left_str, cmp, right_str = split_on_comparator(problem)

    left_ast = parse_side(left_str)
    right_ast = parse_side(right_str)

    step_no = 0

    def show(label: str, eq_str: str) -> None:
        nonlocal step_no
        step_no += 1
        if verbose:
            print(f"Step {step_no} \u2014 {label}:")
            print(f"   {eq_str}\n")

    kind = "equation" if cmp == "=" else "inequality"
    if verbose:
        print(f"Original {kind}:\n   {left_str.strip()} {cmp} {right_str.strip()}\n")

    # --- Step: open brackets -------------------------------------------------
    left_terms = expand(left_ast)
    right_terms = expand(right_ast)
    if has_brackets_to_open(left_ast) or has_brackets_to_open(right_ast):
        show("Opening the brackets",
             f"{format_terms(left_terms)} {cmp} {format_terms(right_terms)}")

    # --- Step: gather like terms ----------------------------------------------
    l_var, l_const = combine(left_terms)
    r_var, r_const = combine(right_terms)
    if needs_combining(left_terms) or needs_combining(right_terms):
        show("Gathering like terms",
             f"{format_side(l_var, l_const)} {cmp} {format_side(r_var, r_const)}")

    # --- Step: clear fractions by multiplying every term by the LCD -----------
    # The LCD (a lowest common multiple of denominators) is always positive,
    # so multiplying both sides by it never flips a comparator.
    lcd = common_denominator(l_var, l_const, r_var, r_const)
    if lcd != 1:
        l_var, l_const, r_var, r_const = l_var * lcd, l_const * lcd, r_var * lcd, r_const * lcd
        show(f"Finding the common denominator (LCD = {lcd}) and multiplying every term by it",
             f"{format_side(l_var, l_const)} {cmp} {format_side(r_var, r_const)}")

    # --- Step: move the variable terms to the left side ----------------------
    # (Adding/subtracting the same amount from both sides never flips a
    # comparator, no matter the sign of that amount -- so 'cmp' is untouched.)
    if r_var != 0:
        l_var, r_var = l_var - r_var, Fraction(0)
        show("Moving the variable terms to the left side",
             f"{format_side(l_var, l_const)} {cmp} {format_side(r_var, r_const)}")

    # --- Step: move the constant terms to the right side ----------------------
    if l_const != 0:
        r_const, l_const = r_const - l_const, Fraction(0)
        show("Moving the constant terms to the right side",
             f"{format_side(l_var, l_const)} {cmp} {format_side(r_var, r_const)}")

    # --- Final step: isolate x -------------------------------------------------
    if l_var == 0:
        is_true = _EVAL[cmp](Fraction(0), r_const)
        if verbose:
            verdict = "every real number is a solution" if is_true else "no solution exists"
            always_never = "always" if is_true else "never"
            print(f"Result: {verdict} "
                  f"(0 {cmp} {fmt_frac(r_const)} is {always_never} true).")
        return Solution("all_reals" if is_true else "no_solution", None, None)

    result = r_const / l_var
    if l_var != 1:
        # Dividing by a negative number is the ONLY operation here that
        # flips an inequality's direction. '=' is never flipped.
        flips = l_var < 0 and cmp != "="
        final_cmp = _FLIP[cmp] if flips else cmp
        label = f"Dividing both sides by {fmt_frac(l_var)}"
        if flips:
            label += " (this flips the inequality sign)"
        show(label, f"x {final_cmp} {fmt_frac(result)}")
    else:
        final_cmp = cmp

    if verbose:
        note = "" if result.denominator == 1 else f"  (\u2248 {float(result):.6g})"
        print(f"\u2705 Solution: x {final_cmp} {fmt_frac(result)}{note}")
    return Solution("unique", final_cmp, result)


# =============================================================================
# 6. CLI / interactive entry point
# =============================================================================

def clear_screen() -> None:
    """Cross-platform 'clear': 'cls' on Windows, 'clear' on macOS/Linux."""
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    if len(sys.argv) > 1:
        equation = " ".join(sys.argv[1:])
        try:
            solve(equation)
        except ValueError as e:
            print(f"Error: {e}")
        return

    print("Linear Equation & Inequality Solver \u2014 type one (e.g. '3x - 2 <= 5x + 1'), "
          "'clear' to clear the screen, or 'quit' to exit.\n")
    while True:
        try:
            eq = input("Equation> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if eq.lower() in ("quit", "exit"):
            break
        if eq.lower() == "clear":
            clear_screen()
            continue
        if eq == "":
            continue
        try:
            solve(eq)
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()