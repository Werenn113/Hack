"""
Solution :
        - on décompile avec godot-unpacker
        - on cat le fichier FlagLabel.gd
        - on a le script suivant :
"""

def flag():
        key = [119, 104, 52, 116, 52, 114, 51, 121, 48, 117, 100, 48, 49, 110, 103, 63]
        enc = [32, 13, 88, 24, 20, 22, 92, 23, 85, 89, 68, 68, 89, 11, 71, 89, 27, 9, 83, 84, 93, 1, 57, 42, 83, 7, 13, 96, 69, 29, 86, 81, 52, 4, 7, 64, 70]

        text = ""
        for i in range(len(enc)):
                text += chr(enc[i] ^ key[i % len(key)])
        return text

if __name__ == "__main__":
        print(flag())