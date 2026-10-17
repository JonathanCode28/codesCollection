password = input("Enter your password: ")

#אתחול של דגלונים עם ערכים בוליאניים
has_letters = False
has_digits = False
has_special = False

#לולאה שתבדוק כל אחד מהדגלונים
for char in password:
    if char.isalpha():
        has_letters = True
    elif char.isdigit():
        has_digits = True
    else:
        has_special = True
        print(has_special)
#בדיקת חוזק הסיסמה
if len(password) < 6:
    print("Password strength: weak (TOO SHORT)")
elif has_digits and has_letters and len(password) <=10:
    print("your password is good.")