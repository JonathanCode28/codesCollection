# Visa Approval Service v3

import time
import random

def intro():
    print("=" * 40)
    print("   VISA APPROVAL SIMULATOR")
    print("        FULL EXPERIENCE")
    print("=" * 40)
    print("\nWelcome, citizen.")
    print("Your ideological compatibility will be evaluated.\n")
    time.sleep(2)

def menu():
    print("\nMAIN MENU")
    print("1. Start evaluation")
    print("2. View system info")
    print("3. Exit")

def system_info():
    print("\nSYSTEM INFO:")
    print("- Version: 1.0")
    print("- Approval Authority: Supreme Administrative Unit")
    print("- Success rate: 100% (official data)")
    print("- Note: All decisions are final.\n")

def get_loyalty():
    loyalty = 50

    print("\nAnswer the following questions:\n")

    q1 = input("Do you fully trust the system? (yes/no): ")
    if q1.lower() == "yes":
        loyalty += 30
    else:
        loyalty -= 20

    q2 = input("Do you enjoy mandatory celebrations? (yes/no): ")
    if q2.lower() == "yes":
        loyalty += 20
    else:
        loyalty -= 10

    q3 = input("Is obedience a positive value? (yes/no): ")
    if q3.lower() == "yes":
        loyalty += 15
    else:
        loyalty -= 15

    return loyalty

def ending(loyalty):
    print("\nAnalyzing results...")
    time.sleep(2)

    print(f"\nFinal loyalty score: {loyalty}%")
    print("-" * 40)

    if loyalty >= 90:
        print("🌟 ULTRA LOYAL ENDING 🌟")
        print("You are promoted to Supreme Enthusiasm Officer.")
        print("Your approval is permanent and unquestionable.")

    elif loyalty >= 70:
        print("✅ APPROVED ENDING")
        print("Your one-way visa to North Korea has been APPROVED.")
        print("Welcome to your new permanent residence.")

    elif loyalty >= 40:
        print("⚠️ PROBATION ENDING")
        print("Your application is delayed indefinitely.")
        print("Please increase enthusiasm and try again.")

    else:
        print("❌ DENIED ENDING")
        print("Your ideological alignment is insufficient.")
        print("You are now under 're-education consideration'.")

def main():
    intro()

    while True:
        menu()
        choice = input("\nSelect option: ")

        if choice == "1":
            loyalty = get_loyalty()
            ending(loyalty)

        elif choice == "2":
            system_info()

        elif choice == "3":
            print("\nShutting down system...")
            time.sleep(1)
            break

        else:
            print("\nInvalid option. Please comply with menu instructions.")

main()