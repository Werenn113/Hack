import socket
import re
import base64
import zlib

host = "challenge01.root-me.org"
port = 52022

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    client.connect((host, port))
    print("Connecté")


    while True:
        data = client.recv(1024).decode()
        print("Réponse du serv : ", data)

        base_64 = re.findall(r"'(.*?)'", data)[0].encode('utf-8')
        print(base_64)

        zlib_str = base64.b64decode(base_64) # type: ignore
        clear_str = zlib.decompress(zlib_str).decode('utf-8')
        
        print(clear_str)
        client.sendall((str(clear_str) + "\n").encode())

finally:
    client.close()