class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def remove_spaces(self, text):
        return text.replace(" ", "")

    def convert_to_upper(self, text):
        return text.upper()

    def generate_extended_key(self, text):
        return (self.key * (len(text) // len(self.key))) + self.key[:len(text) % len(self.key)]

    def encrypt(self, plain_text):
        plain_text = self.remove_spaces(plain_text)
        plain_text = self.convert_to_upper(plain_text)
        extended_key = self.generate_extended_key(plain_text)

        cipher_text = ""
        for i in range(len(plain_text)):
            x = (ord(plain_text[i]) + ord(extended_key[i])) % 26
            x += ord('A')
            cipher_text += chr(x)

        return cipher_text

    def decrypt(self, cipher_text):
        cipher_text = cipher_text.upper()
        extended_key = self.generate_extended_key(cipher_text)

        plain_text = ""
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) - ord(extended_key[i])) % 26
            x += ord('A')
            plain_text += chr(x)

        return plain_text


def main():
    plaintext = "TO BE OR NOT TO BE THAT IS THE QUESTION"
    key = "DOG"

    cipher = VigenereCipher(key)

    print("------------------------------------------------------------")
    print("\n--- Vigenere Cipher ---\n")
    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Extended Key:", cipher.generate_extended_key(plaintext))
    print("Remove Spaces:", cipher.remove_spaces(plaintext))
    print("\n------------------------------------------------------------")

    print("\nProcessing Encrypting and Decrypting...\n")

    print("------------------------------------------------------------")
    encrypted_text = cipher.encrypt(plaintext)
    print("\nEncrypted Text:", encrypted_text)

    decrypted_text = cipher.decrypt(encrypted_text)
    print("\nDecrypted Text:", decrypted_text)
    print("\n------------------------------------------------------------")

if __name__ == '__main__':
    main()

