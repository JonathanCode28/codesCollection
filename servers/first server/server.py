import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))
print("server is running...")
server.listen()

client, addr = server.accept()
run = True
while run:
    client.send(input("what msg?").encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(msg)
server.close()
client.close()