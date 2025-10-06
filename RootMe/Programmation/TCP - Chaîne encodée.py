import socket
import re
import base64

host = "challenge01.root-me.org"
port = 52023

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))
    print("Connecté")
    
    data = client.recv(1024).decode()
    print("Réponse du serv : ", data)

    base64_str = re.findall(r"'(.*?)'", data)[0]
    print(base64_str)
    
    str_clear = base64.b64decode(base64_str).decode('utf-8')
    print(str_clear)

    client.sendall((str(str_clear) + '\n').encode())
    
    data = client.recv(1024).decode()
    print("Réponse du serv : ", data)
                             
    
finally:
    client.close()