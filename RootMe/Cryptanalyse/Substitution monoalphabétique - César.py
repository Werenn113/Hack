from string import ascii_lowercase
import re

text = "tm bcsv qolfp f'dmvd xuhm exl tgak hlrkiv sydg hxm qiswzzwf qrf oqdueqe dpae resd wndo liva bu vgtokx sjzk hmb rqch fqwbg fmmft seront sntsdr pmsecq"

def caesar_decrypt(text, shift):
    plain_text = ""
    for char in text:
        if char in ascii_lowercase:
            plain_text += ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]
        else:
            plain_text += char
    print(plain_text)
    return plain_text

if __name__ == "__main__":
    plain_text = ""
    for i in range(1, 26):
        words = re.split(r'[^' + ascii_lowercase + r']+', caesar_decrypt(text, i))
        plain_text += (words[i-1] + " ")
    print(plain_text)

# ujqcsdde