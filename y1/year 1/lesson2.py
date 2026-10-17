import random

# Dinyamic writing in python
name = "cactus"
age = 123

print(f"Hello my name is {name} and i'm {age} years old")

random_number = random.randint(1, 100)
print(f"the random number is {random_number}")

if random_number > 50:
    print(f"{random_number} is graeter then 50")
else:
    print(f"{random_number} is smaller then 50")