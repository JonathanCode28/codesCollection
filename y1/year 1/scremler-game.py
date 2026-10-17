import random

#הגדרת רשימה עם בנק מילים
words = ["boeing", "airbus", "pilot", "cabin", "aviation", "flight", "airplane"]

#בחירת אופציה אקראית מבנק המילים
secret_word = random.choice(words)
scremble_word = random.sample(secret_word, len(secret_word))

s_word = "".join(scremble_word)

print("Unscremble the word")
print(f"scambled word: {s_word}")

attempts = 3

while attempts > 0:
    guess = input("What is your guess: ")

    if guess.lower() == secret_word:
        print(f"Correct! the word is {secret_word}. You win!")
        break
    else:
        attempts -=1
        if attempts > 0:
            print(f"Wrong! try again. {attempts} attempts left")
        else:
            print(f"Out of attempts! the correct answer is {secret_word}. You lose...")