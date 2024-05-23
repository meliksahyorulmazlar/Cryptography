#Caesar Cipher


class CaesarCipher:
    def __init__(self):
        self.alphabet:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']

    def encrypt(self,text:str,shift:int):
        new_letters:list = []
        text = text.lower()
        for letter in text:
            if letter in self.alphabet:
                position = (self.alphabet.index(letter) +shift) % 26
                new_letters.append(self.alphabet[position])
            else:
                new_letters.append(letter)
        print("".join(new_letters))

    def decrypt(self,text:str,shift:int):
        new_letters = []
        text = text.lower()
        for letter in text:
            if letter in self.alphabet:
                position = (self.alphabet.index(letter) -shift) % 26
                new_letters.append(self.alphabet[position])
            else:
                new_letters.append(letter)
        print("".join(new_letters))

caesar = CaesarCipher()
caesar.decrypt("pholnvdk",3)
