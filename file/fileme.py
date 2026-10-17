name = input("give me your name: ")
line1 = input("short story: ")

file = open("myfile.txt", "w")
file.write(f"name: {name} \n")
file.write(line1 + "\n")
file.close()

file = open("myfile.txt", "r")
print(file.read())
file.close()

file = open("myfile.txt", "a")
line2 = input("short story2")