# Visa Approval Service v2
import time
import random

print("===================================")
print("   VISA APPROVAL SIMULATOR")
print("        DEMO VERSION")
print("===================================\n")

name = input("Enter your name: ")
country = input("Choose destination country: ")

print("\nInitializing government database...")
time.sleep(2)

# "loyalty" system
loyalty = 50

print("\nAnswer a few questions to assess loyalty:\n")

q1 = input("Do you support the Supreme Leader? (yes/no): ")
if q1.lower() == "yes":
    loyalty += 30
else:
    loyalty -= 20

q2 = input("Do you enjoy national parades? (yes/no): ")
if q2.lower() == "yes":
    loyalty += 20
else:
    loyalty -= 10

q3 = input("Is your favorite color red? (yes/no): ")
if q3.lower() == "yes":
    loyalty += 10
else:
    loyalty -= 5

print("\nAnalyzing responses...")
time.sleep(2)

print(f"\nFinal loyalty score: {loyalty}%")
print("-" * 30)

print("Processing visa request...")
time.sleep(3)

approved_chance = loyalty + random.randint(-20, 20)

print("\nRESULT:")

if approved_chance >= 70:
    print(f"APPROVED ✅")
    print(f"Dear {name}, your one-way visa to North Korea has been approved.")
    print("We wish you a permanent and peaceful stay.")
else:
    print("DENIED ❌")
    print("Reason: insufficient ideological alignment.")
    print("Please reconsider your values and try again later.")