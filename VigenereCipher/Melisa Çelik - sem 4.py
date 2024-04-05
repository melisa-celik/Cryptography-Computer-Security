# Student Name & Surname: Melisa Çelik
# Student ID: CEL0052

from time import sleep

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def extendKey(self, plaintext):
        extendedKey = ''
        keyLength = len(self.key)
        plaintextLength = len(plaintext)
        repetitions = plaintextLength // keyLength
        remainder = plaintextLength % keyLength
        extendedKey += self.key * repetitions
        extendedKey += self.key[:remainder]
        return extendedKey

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        extendedKey = self.extendKey(plaintext)
        ciphertext = ''
        for i in range(len(plaintext)):
            shift = self.alphabet.index(extendedKey[i])
            shiftedIndex = (self.alphabet.index(plaintext[i]) + shift) % 26
            ciphertext += self.alphabet[shiftedIndex]
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper().replace(" ", "")
        extendedKey = self.extendKey(ciphertext)
        plaintext = ''
        for i in range(len(ciphertext)):
            shift = self.alphabet.index(extendedKey[i])
            shiftedIndex = (self.alphabet.index(ciphertext[i]) - shift) % 26
            plaintext += self.alphabet[shiftedIndex]
        return plaintext

def getValidKey():
    while True:
        try:
            choice = input("Do you want to enter a custom key? If no, the default key 'KEY' will used (yes/no): ").strip().lower()
            if choice == 'yes':
                key = input("Enter the key (a word without spaces): ").upper()
                if key.isalpha():
                    print("Setting the key...")
                    sleep(1)
                    print("Using custom key:", key)
                    return key
                else:
                    print("\nInvalid key. Key should be a word without spaces.")
                    print("Please try again:\n")
            elif choice == 'no':
                print("Setting the key...")
                sleep(1)
                print("Using default key: 'KEY'")
                return "KEY"
            else:
                print("\nInvalid choice. Please enter 'yes' or 'no'.")
                print("Please try again:\n")
        except ValueError:
            print("\nInvalid input.")
            print("Please enter a word without spaces:\n")


def upperCase(text):
    return text.upper()

def omitSpaces(text):
    return text.replace(" ", "")


def main():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n--- Vigenere Cipher ---\n")

    # Key: KEY
    key = getValidKey()

    cipher = VigenereCipher(key)

    plaintext = "TO BE OR NOT TO BE THAT IS THE QUESTION"
    print("\nPlaintext:", plaintext)
    print("\nPreparing the plaintext for encryption...\n")
    sleep(0.1)
    print("Converting to uppercase...")
    sleep(0.2)
    plaintext = upperCase(plaintext)
    print("Uppercase Conversion Completed!\n")
    sleep(0.1)
    print("Omitting spaces...")
    sleep(0.2)
    plaintext = omitSpaces(plaintext)
    print("Spaces Omitted!\n")
    sleep(0.2)
    print("Plaintext after preparation:", plaintext)

    print("\nProcessing Encrypting with Vigenere Cipher...")
    sleep(1)
    encryptedText = cipher.encrypt(plaintext)
    print("Encryption Completed!")
    print("Encrypted Text:", encryptedText)
    sleep(0.1)
    print("\nProcessing Decrypting with Vigenere Cipher...")
    sleep(1)
    decryptedText = cipher.decrypt(encryptedText)
    print("Decryption Completed!")
    print("Decrypted Text:", decryptedText)

    sleep(0.5)
    print("\nVigenere Cipher Encryption and Decryption Completed!")
    sleep(0.5)
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
