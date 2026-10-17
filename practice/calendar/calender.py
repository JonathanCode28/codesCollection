import calendar

print("Calender Program")

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print("\nHere is the calendar:\n")
print(calendar.month(year, month))