#פונקציה היא דבר שימושי שמייעל עבורנו את הכתיבהבכך שלא צריך לכתוב את אותו קטע של קוד פעמיים

def greet(): #הגדרת הפונקציה
    print("Hello Uֹser") #תןכן הפונקציה
greet() #הקריאה לפונקציה לפעולה
def s_greet(name):
    print(f"hello {name}")
s_greet(123)
s_greet("sicilian")
s_greet("modern")
s_greet("king's pawn")
s_greet("queen's pawn opening")
s_greet("karo-kann defence")
def plus(a,b):
    if type(a) == "string" and type(b) == "string":
        result = a + " " + b
        return result
    else:
        return a+b
print(plus("good ", "day"))
