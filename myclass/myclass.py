class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def greet(self):
        try:
            print(f"hi im {self.name}")
            print(x)
        except NameError as e:
            print(f"error: {e}")
player1 = Hero("Elon-Busk", "money")
player1.greet()
player2 = Hero("Superman", "just a nice guy")
player2.greet()
print(player1.name, player1.power)
print(player2.name, player2.power)
