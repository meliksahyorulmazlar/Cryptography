#ROT13 Cipher


class Rot13:
    def __init__(self):
        self.alphabet_lower:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
        self.alphabet_upper:list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.shift:int = 13
    def encrypt(self,text:str)->None:
        new_letters:list = []
        for char in text:
            if char in self.alphabet_lower:
                position = (self.alphabet_lower.index(char) +self.shift) % 26
                new_letters.append(self.alphabet_lower[position])
            elif char in self.alphabet_upper:
                position = (self.alphabet_upper.index(char) +self.shift) % 26
                new_letters.append(self.alphabet_upper[position])
            else:
                new_letters.append(char)
        print("".join(new_letters))

    def decrypt(self,text:str)->None:
        new_letters:list = []
        for char in text:
            if char in self.alphabet_lower:
                position = (self.alphabet_lower.index(char) -self.shift) % 26
                new_letters.append(self.alphabet_lower[position])
            elif char in self.alphabet_upper:
                position = (self.alphabet_upper.index(char) -self.shift) % 26
                new_letters.append(self.alphabet_upper[position])
            else:
                new_letters.append(char)
        print("".join(new_letters))

    """
    the decrypt method is the same thing as self.encrypt(text,-shift)
    """

if __name__ == "__main__":
    rotate = Rot13()
    user_text:str = input('What text would you like to encrypt or decrypt with the ROT13 cipher?\n')
    type:str = input("Do you want to encrypt or decrypt")
    if type.lower() == "decrypt":
        rotate.decrypt(user_text)
    else:
        rotate.encrypt(user_text)
