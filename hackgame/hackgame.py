#!/usr/bin/env python3
"""
  ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
  ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
  ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
         TERMINAL HACK SIM v1.0  |  by Claude
"""

import time, random, sys, os

# ── ANSI colors ──────────────────────────────────────────────────────────────
G  = "\033[92m"   # bright green
R  = "\033[91m"   # red
Y  = "\033[93m"   # yellow
C  = "\033[96m"   # cyan
W  = "\033[97m"   # white
DG = "\033[32m"   # dark green
RS = "\033[0m"    # reset
BOLD = "\033[1m"

def clr(): os.system("cls" if os.name == "nt" else "clear")

# ── Helpers ───────────────────────────────────────────────────────────────────
def slow(text, delay=0.03, color=G):
    for ch in text:
        sys.stdout.write(color + ch + RS)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_progress(label, steps=20, color=G):
    sys.stdout.write(f"  {color}{label}{RS}  [")
    for i in range(steps):
        time.sleep(random.uniform(0.03, 0.12))
        sys.stdout.write(f"{color}#{RS}")
        sys.stdout.flush()
    print(f"]  {G}DONE{RS}")

def glitch_text(text, rounds=3):
    chars = "!@#$%^&*<>?/\\|~"
    for _ in range(rounds):
        corrupted = "".join(
            random.choice(chars) if random.random() < 0.4 else c
            for c in text
        )
        sys.stdout.write(f"\r  {Y}{corrupted}{RS}")
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write(f"\r  {G}{text}{RS}\n")

def rand_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def rand_hex(n=32):
    return "".join(random.choices("0123456789abcdef", k=n))

def divider(c="═", color=DG):
    print(color + c * 60 + RS)

# ── Banner ────────────────────────────────────────────────────────────────────
def banner():
    clr()
    print(G + BOLD + __doc__ + RS)
    divider()

# ── Intro cutscene ────────────────────────────────────────────────────────────
def intro():
    banner()
    slow("  Initializing secure shell...", color=DG)
    time.sleep(0.4)
    fake_progress("Loading exploit modules  ", 15)
    fake_progress("Spoofing MAC address     ", 10)
    fake_progress("Routing through Tor      ", 18)
    print()
    slow("  Welcome, Agent.", color=C)
    slow("  Your mission: breach NEXUS-7, the corporate mainframe.", color=W)
    slow("  You have 5 hacking tools. Use them wisely.", color=W)
    print()
    input(f"  {Y}[ Press ENTER to begin ] {RS}")

# ── Game state ────────────────────────────────────────────────────────────────
class GameState:
    def __init__(self):
        self.target_ip  = rand_ip()
        self.security   = 100          # firewall strength
        self.trace      = 0            # FBI trace %
        self.files      = []
        self.log        = []
        self.turn       = 0
        self.max_turns  = 10
        self.score      = 0
        # Secrets to steal
        self.vault = {
            "passwords.enc":  False,
            "financial.db":   False,
            "blueprints.zip": False,
            "admin_keys.pem": False,
        }

    @property
    def breached(self):
        return self.security <= 0

    @property
    def caught(self):
        return self.trace >= 100

    @property
    def files_stolen(self):
        return sum(self.vault.values())

# ── HUD ───────────────────────────────────────────────────────────────────────
def draw_hud(gs):
    divider()
    sec_bar = int(gs.security / 5)
    trc_bar = int(gs.trace / 5)
    sec_col = G if gs.security > 50 else (Y if gs.security > 20 else R)
    trc_col = G if gs.trace < 40 else (Y if gs.trace < 70 else R)
    print(f"  {C}TARGET{RS}  {gs.target_ip:<18}"
          f"  {C}TURN{RS}  {gs.turn}/{gs.max_turns}")
    print(f"  {C}FIREWALL{RS}  {sec_col}{'█'*sec_bar}{'░'*(20-sec_bar)}{RS} {gs.security:>3}%"
          f"   {C}TRACE{RS}  {trc_col}{'█'*trc_bar}{'░'*(20-trc_bar)}{RS} {gs.trace:>3}%")
    stolen = [k for k,v in gs.vault.items() if v]
    print(f"  {C}FILES STOLEN{RS}  {G}{', '.join(stolen) if stolen else 'none'}{RS}")
    divider()

# ── Tools / actions ───────────────────────────────────────────────────────────
def tool_portscan(gs):
    slow("  [PORTSCAN] Scanning open ports...", color=DG)
    ports = random.sample([21,22,80,443,3306,5432,8080,27017], k=4)
    time.sleep(0.5)
    for p in ports:
        svc = {21:"FTP",22:"SSH",80:"HTTP",443:"HTTPS",
               3306:"MySQL",5432:"PostgreSQL",8080:"HTTP-ALT",27017:"MongoDB"}.get(p,"Unknown")
        print(f"    {G}PORT {p:>5}  OPEN  →  {svc}{RS}")
        time.sleep(0.15)
    reduction = random.randint(5, 15)
    gs.security -= reduction
    gs.trace    += random.randint(0, 5)
    gs.score    += 10
    gs.log.append(f"Portscan: -{reduction}% firewall")
    slow(f"  Firewall weakened by {reduction}%", color=Y)

def tool_exploit(gs):
    slow("  [EXPLOIT] Launching buffer-overflow payload...", color=DG)
    glitch_text("0x7ffd4a3c1b28  →  OVERFLOW  →  SHELL ACQUIRED")
    time.sleep(0.3)
    success = random.random() < (0.8 - gs.security / 200)
    if success:
        reduction = random.randint(20, 35)
        gs.security -= reduction
        gs.trace    += random.randint(5, 15)
        gs.score    += 30
        gs.log.append(f"Exploit: -{reduction}% firewall")
        slow(f"  {G}SUCCESS! Firewall -" + str(reduction) + "%" + RS, color=G)
    else:
        gs.trace += random.randint(10, 20)
        gs.score -= 5
        gs.log.append("Exploit: FAILED, trace +")
        slow(f"  {R}EXPLOIT FAILED — IDS triggered! Trace increased.{RS}", color=R)

def tool_steal(gs):
    if gs.security > 40:
        slow(f"  {R}[STEAL] Firewall too strong! Weaken it first.{RS}", color=R)
        return
    available = [k for k,v in gs.vault.items() if not v]
    if not available:
        slow(f"  {Y}[STEAL] No more files to steal.{RS}", color=Y)
        return
    target_file = random.choice(available)
    slow(f"  [STEAL] Accessing {target_file}...", color=DG)
    fake_progress(f"Copying {target_file:<20}", 12)
    gs.vault[target_file] = True
    gs.trace += random.randint(5, 12)
    gs.score += 50
    gs.log.append(f"Stolen: {target_file}")
    slow(f"  {G}File secured: {target_file}{RS}", color=G)

def tool_cover(gs):
    slow("  [COVER TRACKS] Wiping logs...", color=DG)
    fake_progress("Deleting syslog entries  ", 14)
    reduction = random.randint(15, 30)
    gs.trace = max(0, gs.trace - reduction)
    gs.score += 15
    gs.log.append(f"Cover tracks: trace -{reduction}%")
    slow(f"  {G}Trace reduced by {reduction}%{RS}", color=G)

def tool_ddos(gs):
    slow("  [DDoS] Flooding firewall with junk traffic...", color=DG)
    for _ in range(5):
        ip = rand_ip()
        sys.stdout.write(f"    {DG}→ {ip}  payload: {rand_hex(16)}{RS}\n")
        time.sleep(0.1)
    reduction = random.randint(10, 25)
    gs.security -= reduction
    gs.trace    += random.randint(3, 10)
    gs.score    += 20
    gs.log.append(f"DDoS: -{reduction}% firewall")
    slow(f"  {G}Firewall disrupted by {reduction}%{RS}", color=G)

TOOLS = [
    ("PORTSCAN",      "Map open ports, weaken firewall slightly",    tool_portscan),
    ("EXPLOIT",       "High-risk payload — big damage or big trace", tool_exploit),
    ("STEAL FILES",   "Grab vault files (firewall must be < 40%)",   tool_steal),
    ("COVER TRACKS",  "Reduce FBI trace percentage",                 tool_cover),
    ("DDoS BLAST",    "Flood & weaken firewall fast",                tool_ddos),
]

def pick_tool(gs):
    print(f"\n  {C}Choose your tool:{RS}")
    for i, (name, desc, _) in enumerate(TOOLS, 1):
        print(f"  {Y}[{i}]{RS}  {G}{name:<14}{RS}  {W}{desc}{RS}")
    print()
    while True:
        try:
            choice = int(input(f"  {C}> {RS}")) - 1
            if 0 <= choice < len(TOOLS):
                return TOOLS[choice]
        except (ValueError, KeyboardInterrupt):
            pass
        print(f"  {R}Invalid choice. Enter 1-{len(TOOLS)}.{RS}")

# ── Ending screens ─────────────────────────────────────────────────────────────
def ending_caught(gs):
    clr()
    slow("  ██╗██████╗ ███████╗    ████████╗██████╗  █████╗  ██████╗███████╗██████╗ ", delay=0.01, color=R)
    slow("  ██║██╔══██╗██╔════╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗", delay=0.01, color=R)
    slow("  ██║██████╔╝███████╗       ██║   ██████╔╝███████║██║     █████╗  ██║  ██║", delay=0.01, color=R)
    slow("  ██║██╔═══╝ ╚════██║       ██║   ██╔══██╗██╔══██║██║     ██╔══╝  ██║  ██║", delay=0.01, color=R)
    slow("  ██║██║     ███████║       ██║   ██║  ██║██║  ██║╚██████╗███████╗██████╔╝", delay=0.01, color=R)
    slow("  ╚═╝╚═╝     ╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝ ", delay=0.01, color=R)
    print()
    slow("  The FBI traced your signal. Agents are at the door.", color=W)
    slow(f"  Files stolen: {gs.files_stolen}/4   Score: {gs.score}", color=Y)
    print(f"\n  {R}GAME OVER{RS}\n")

def ending_timeout(gs):
    clr()
    slow("  TIME'S UP — Server auto-wiped.", color=Y)
    slow(f"  Files stolen: {gs.files_stolen}/4   Score: {gs.score}", color=Y)
    if gs.files_stolen == 0:
        slow("  You got nothing. Try faster next time.", color=R)
    elif gs.files_stolen < 3:
        slow("  Partial success. The corporation suspects a breach.", color=Y)
    else:
        slow("  Nearly a clean sweep. Impressive.", color=G)
    print(f"\n  {Y}MISSION INCOMPLETE{RS}\n")

def ending_win(gs):
    clr()
    slow("  ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗██╗", delay=0.01, color=G)
    slow("  ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██║", delay=0.01, color=G)
    slow("  ██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ ██║", delay=0.01, color=G)
    slow("  ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  ╚═╝", delay=0.01, color=G)
    slow("   ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   ██╗", delay=0.01, color=G)
    slow("    ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝", delay=0.01, color=G)
    print()
    slow(f"  All {gs.files_stolen} files extracted. NEXUS-7 is yours.", color=W)
    slow(f"  Final score: {gs.score}  |  Turns used: {gs.turn}/{gs.max_turns}", color=C)
    print(f"\n  {G}MISSION ACCOMPLISHED{RS}\n")

# ── Main loop ─────────────────────────────────────────────────────────────────
def game_loop():
    gs = GameState()
    while gs.turn < gs.max_turns:
        clr()
        banner()
        draw_hud(gs)

        # Check win
        if gs.files_stolen == len(gs.vault) and gs.breached:
            ending_win(gs)
            return

        # Check lose
        if gs.caught:
            ending_caught(gs)
            return

        # Pick & execute tool
        name, _, fn = pick_tool(gs)
        print()
        fn(gs)
        gs.turn += 1
        print()
        input(f"  {DG}[ Press ENTER to continue ]{RS}")

    # Out of turns
    ending_timeout(gs)

# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    try:
        intro()
        game_loop()
        print(f"  {C}Thanks for playing HACKER SIM!{RS}\n")
    except KeyboardInterrupt:
        print(f"\n\n  {R}Connection terminated.{RS}\n")

if __name__ == "__main__":
    main()
