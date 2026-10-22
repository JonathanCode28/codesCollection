# elections in North Korea Simulator
import time

print("Please vote:")
print("1. Kim Jong Un")
print("2. Not Kim Jong Un")
print("-" * 10)

vote = int(input("Enter the number of your vote: "))

if vote == 1:
    print("Thank you for voting.")
elif vote == 2:
    print("HOW DARE YOU?!")
    time.sleep(2)
    print("You should already know what's waiting for you.")
    time.sleep(2)
    print("🔫☠️")
    time.sleep(2)
    print("And your vote has will not be counted.")
else:
    print("Invalid vote.")
    print("Your vote has been corrected.")

print("Counting votes...")
time.sleep(2)

print("Kim Jong Un: 100%")
print("Not Kim Jong Un: 0%")
print("Congratulations! The people have spoken.")