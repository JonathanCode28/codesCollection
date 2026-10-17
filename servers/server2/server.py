import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))
print("server is running...")
server.listen()

client, addr = server.accept()
greetings = [
   "Hello!",
   "Hi there!",
   "Greetings!",
   "Good day!",
   "Hey!",
   "Nice to meet you!",
   "Howdy!",
   "Salutations!",
   "Hey, what's up?",
   "Welcome!"
]
A = "greet"

run = True
while run:
    msg = client.recv(1024).decode("utf-8")
    print(f"client: {msg}")
    if A == "greet":
        client.send(random.choice(greetings).encode("utf-8"))
        A = "name"
    elif A == "name":
        client.send("what is your name?".encode("utf-8"))
    server.close()
    client.close()