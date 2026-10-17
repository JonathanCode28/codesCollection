import random

random_number = random.randint(1, 50)
counter = 0
#print(random_number, counter)
while True:
    user_guess = int(input("Guess a number from 1 to 50. Your number:"))
    counter += 1

    #print(user_guess)
    if user_guess > random_number:
        print('Too high!! try again!!')
    elif user_guess < random_number:
        print("Too low!! try again!!")
    else:
        print(f"Very good. You made it in {counter} guess.")
        break