import socket
import re

host = "challenge01.root-me.org"
port = 52002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))
    print("Connecté")
    
    data = client.recv(1024).decode()
    print("Réponse du serv : ", data)
    
    nombres = re.findall(r'\d+', data)[1:]
    print(nombres)
    
    calc = round(int(nombres[0])**0.5 * int(nombres[1]), 2)
    print(calc)
    
    client.sendall((str(calc) + '\n').encode())
    
    data = client.recv(1024).decode()
    print("Réponse du serv : ", data)
                                         
    
finally:
    client.close()