num1 = float(input("choose a number:"))
num2 = float(input("choose another number:"))
oper = input("choose an operation (+, -, *, /, **):")

if oper == "+":
    res = num1+num2
elif oper == "-":
    res = num1-num2
elif oper == "*":
    res = num1*num2
elif oper == "/" and num2 != 0:
    res = num1/num2
elif oper == "**":
    res = num1**num2
else:
    res = "invalid operation, please choose valid operation"
print("the result is: ", res)