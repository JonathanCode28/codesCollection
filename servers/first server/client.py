import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

run = True
while run:
    msg = client.recv(1024).decode("utf-8")
    client.send(input("what msg?").encode("utf-8"))
    print(msg)
client.close()
