#valeur de ch7 en hexa pour l’obtenir : xxd ch7.bin
ch7='\x4c\x7c\x6b\x80\x79\x2b\x2a\x5e\x7f\x2a\x7a\x6f\x7f\x82\x2a\x80\x6b\x76\x73\x6e\x6f\x7c\x2a\x6b\x80\x6f\x6d\x2a\x76\x6f\x2a\x7a\x6b\x7d\x7d\x2a\x63\x79\x76\x6b\x73\x72\x7f\x14\x0a'
 
# Pour chaque décalage possible de 0 à 255
for decalage in range(256):
    # On décale chaque caractère de ch7, puis on les assemble en une chaîne
    texte_decode = ''.join([chr((ord(caractere) + decalage) % 256) for caractere in ch7])
    # On affiche le décalage et le texte décodé correspondant
    print(f"{decalage}: {repr(texte_decode)}")