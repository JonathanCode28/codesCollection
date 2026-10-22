import time
import random
import sys

# ---------- ANIMATION HELPERS ----------

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading(text, duration=3):
    print(text)
    for i in range(duration * 3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\n")

def clear_section():
    print("\n" + "-" * 50 + "\n")


# ---------- INTRO SCREEN ----------

def intro():
    print("=" * 50)
    slow_print("   VISA APPROVAL SIMULATOR 2")
    slow_print("       TERMINAL EDITION")
    print("=" * 50)
    print()
    slow_print("Booting government terminal...")
    loading("Loading system modules", 3)
    slow_print("Connection established with Central Authority.")
    slow_print("Welcome, citizen.\n")
    time.sleep(1)


# ---------- MENU ----------

def menu():
    clear_section()
    print("MAIN MENU")
    print("1. Start visa evaluation")
    print("2. System information")
    print("3. Exit")
    print()


# ---------- SYSTEM INFO ----------

def system_info():
    clear_section()
    slow_print("SYSTEM INFORMATION")
    print()
    slow_print("Version: TERMINAL BUILD")
    slow_print("Authority: Supreme Administrative Network")
    slow_print("Status: ALWAYS OPTIMAL")
    slow_print("Error tolerance: 0%")
    print()
    input("Press Enter to return...")


# ---------- LOYALTY TEST ----------

def get_loyalty():
    clear_section()
    slow_print("INITIALIZING PERSONALITY SCAN...\n")
    loading("Analyzing behavioral patterns", 2)

    loyalty = 50

    q1 = input("Do you trust the system? (yes/no): ")
    if q1.lower() == "yes":
        loyalty += 30
    else:
        loyalty -= 20

    q2 = input("Do you enjoy national celebrations? (yes/no): ")
    if q2.lower() == "yes":
        loyalty += 20
    else:
        loyalty -= 10

    q3 = input("Do you love the Supreme Leader? (yes/no): ")
    if q3.lower() == "yes":
        loyalty += 15
    else:
        loyalty -= 15

    clear_section()
    loading("Finalizing analysis", 2)

    return loyalty


# ---------- ENDINGS ----------

def ending(loyalty):
    print("\n" + "=" * 50)
    slow_print("FINAL RESULTS PROCESSING...\n")
    time.sleep(1)

    slow_print(f"Loyalty Score: {loyalty}%\n")

    if loyalty >= 90:
        slow_print("🌟 ULTRA LOYAL ENDING 🌟")
        slow_print("You are promoted to Supreme Enthusiasm Officer.")
        slow_print("Access level: UNLIMITED")
        slow_print("Status: PERMANENT APPROVAL")

    elif loyalty >= 70:
        slow_print("✅ APPROVED ENDING")
        slow_print("Your one-way visa has been APPROVED.")
        slow_print("Destination locked: North Korea")
        slow_print("Status: IRREVERSIBLE")

    elif loyalty >= 40:
        slow_print("⚠️ PROBATION ENDING")
        slow_print("Application delayed indefinitely.")
        slow_print("System recommends increased enthusiasm.")

    else:
        slow_print("❌ DENIED ENDING")
        slow_print("Ideological alignment insufficient.")
        slow_print("User flagged for review.")
        slow_print("Status: ACCESS RESTRICTED")

    print("\n" + "=" * 50)
    input("\nPress Enter to return to menu...")


# ---------- MAIN LOOP ----------

def main():
    intro()

    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            loyalty = get_loyalty()
            ending(loyalty)

        elif choice == "2":
            system_info()

        elif choice == "3":
            slow_print("\nShutting down system...")
            loading("Closing secure connection", 2)
            break

        else:
            slow_print("Invalid command. Please comply with system format.")


main()