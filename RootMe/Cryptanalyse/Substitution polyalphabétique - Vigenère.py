def get_key(ciphertext, plain_text):
    key = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            key += chr((ord(ciphertext[i]) - ord(plain_text[i])) % 26 + ord('a'))
        else:
            key += ciphertext[i]
    return key

def vigenere_decrypt(ciphertext, key):
    plain_text = ""
    key_length = len(key)
    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            plain_text += chr(((ord(ciphertext[i].upper()) - ord(key[j % key_length].upper())) % 26) + ord('A'))
            j += 1
        else:
            plain_text += ciphertext[i]
    return plain_text

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    
def rotation(text, n):
    return text[n:] + text[:n]


if __name__ == "__main__":
    # print(get_key("ehcclkk'lgm", "aujourd'hui"))
    # print(get_key("nnxfnyh'tyv", "aujourd'hui"))

    file = read_file("ch11.txt")
    # key = "NTORTHEME"  # clé en MAJUSCULES
    # for i in range(len(key)):
    #     rotation_key = rotation(key, i)
    #     print(f"Essai avec clé : {rotation_key}")
    #     print(vigenere_decrypt(file, rotation_key))

    print(vigenere_decrypt(file, "THEMENTOR"))

    ### On fait une recherche the hacker manifesto thementor