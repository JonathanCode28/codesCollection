import random
class Superpet:
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower
        self.power_level = random.randint(0, 10)
    def info(self):
        print(f"name: {self.name} superpower: {self.superpower}")
    def guess_power_level(self):
        user_guess = input("Enter your guess for the superhero's power level (between 0 and 10): ")
        user_guess = int(user_guess)
        if user_guess < self.power_level:
            print("small")
            self.guess_power_level()
        elif user_guess > self.power_level:
            print("big")
            self.guess_power_level()
        elif user_guess == self.power_level:
            print("cheater")
player1 = Superpet("kripto", "superbark")
player1.info()
player1.guess_power_level()