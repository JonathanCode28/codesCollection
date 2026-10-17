year = input("Enter a year: ")

if year.isdigit():
    year = int(year)
    if year%4 == 0 and year%100 != 0:
        print("This year will be a leap year.")
User_number = input("Please choose a number: ")

if User_number.isdigit():
    int(User_number)
    if User_number%2 == 0:
        print("your number is even number")
    elif User_number%2 == 1:
         print("your number is don't an even number")
    else:
        print("Please enter valid number")
