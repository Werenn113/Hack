import socket
import re
import codecs

host = "challenge01.root-me.org"
port = 52021

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((host, port))
    print("Connecté")
    
    data = client.recv(1024).decode()
    print("Réponse du serv : ", data)

    rot13_str = re.findall(r"'(.*?)'", data)[0]
    print(rot13_str)
    
    str_clear = codecs.decode(rot13_str, 'rot13')
    print(str_clear)

    client.sendall((str(str_clear) + '\n').encode())
    
    data = client.recv(1024).decode()
    print("Réponse du serv : ", data)
                             
    
finally:
    client.close()