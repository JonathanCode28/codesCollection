# National News Generator
import random

news = [
    "Our great Supreme Leader defeated a supercomputer in chess.",
    "The sun rose earlier to honor the Leader",
    "North Korea has won the World Cup for the 12th consecutive time.",
    "The harvest increased by 700%!",
    "The Supreme Leader has successfully invented a new color that only loyal citizens can see.",
    "All citizens report 100% satisfaction with today’s weather, food, and existence.",
    "North Korea has officially solved world hunger by declaring it does not exist.",
    "Scientists confirm the Leader’s wisdom is measurable in infinite units.",
    "The national economy has grown by 1,000% after a motivational speech.",
    "A new law has been passed making happiness mandatory — compliance is already 100%."
]

for i in range(1, 6):
    print(f"{i}. {random.choice(news)}")
    print("-"*30)