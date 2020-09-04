import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('IP', port))

while True:
    try:
        data = input()
        data = data.encode('UTF-8')
        client.sendall(data)
        recv = client.recv(1024)
        print(recv)
    except:
        pass

client.close()