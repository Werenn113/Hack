"""
Pour trouver la clé XOR: 
    On sait que l'image est en BMP, et que les 14 premiers octets sont toujours les mêmes :
        42 4d       correspond au type de fichier (caractères B et M)
        f6 8f 07 00 taille en octets de l'image. Dans notre cas, la taille est de 495 606 octets donc 00078FF6. Il faudra inverser les octets
        00 00 00 00 Réservé, toujours égal à zéro.
        36 00 00 00 Offset de l'image, toujours identique
    On récupère alors les 14 premiers octets de l'image chiffrée et on les xor avec les valeurs connues.
    On décode le hex en ascii et on voit la clé fallen qui se répète.
"""

from PIL import Image

def xor_decrypt(input_path, output_path, key):
    with open(input_path, "rb") as f_in:
        data = f_in.read()
    key_len = len(key)
    decrypted = bytearray()
    for i, byte in enumerate(data):
        decrypted.append(byte ^ key[i % key_len])
    with open(output_path, "wb") as f_out:
        f_out.write(decrypted)

# Ta clé sous forme de chaîne
key_str = "fallen"
key = key_str.encode()  # Conversion en bytes

# Déchiffrer l'image
xor_decrypt("C:/Users/baptm/Downloads/ch3.bmp", "image_dechiffree.bmp", key)

img = Image.open("image_dechiffree.bmp")
img.show()  # Afficher l'image déchiffrée