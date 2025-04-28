import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 12345))
done = False
while not done:
    client.send(input("Enter message: ").encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    if msg == "exit":
        done = True
    else:
        print(msg)

client.close()
