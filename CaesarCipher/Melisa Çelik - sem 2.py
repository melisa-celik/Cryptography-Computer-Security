# Student Name & Surname: Melisa Çelik
# Student ID: CEL0052

from time import sleep

class CaesarCipher:
    def __init__(self, shift):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.shift = shift

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha() and char.isupper():
                shiftedIndex = (self.alphabet.index(char) + self.shift) % 26
                ciphertext += self.alphabet[shiftedIndex]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha() and char.isupper():
                shiftedIndex = (self.alphabet.index(char) - self.shift) % 26
                plaintext += self.alphabet[shiftedIndex]
            else:
                plaintext += char
        return plaintext

def implementBruteForceAttack(ciphertext):
    for key in range(26):
        sleep(0.25)
        cipher = CaesarCipher(key)
        decryptedText = cipher.decrypt(ciphertext)
        print(f"Key: {key}, \tDecrypted Text:\t {decryptedText}")
        sleep(0.25)

def getValidShift():
    while True:
        try:
            shift = int(input("Enter the shift value (an integer between 0 and 25): "))
            if shift < 0 or shift > 25:
                print("\nInvalid shift value. Shift should be between 0 and 25.")
                print("Please try again:\n")
            else:
                return shift
        except ValueError:
            print("\nInvalid input.")
            print("Please enter an integer:\n")

def main():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n--- Caesar Cipher ---\n")

    shift = getValidShift()

    cipher = CaesarCipher(shift)

    ciphertext = "AOPZALYTPUHSPZUVTVYLPAOHZJLHZLKAVILPAZLEWPYLKHUKNVULAVT LAPAZTHRLYAOPZPZHSHALALYTPUHSPAZHZAPMMILYLMAVMSPMLPAYLZA PUWLHJLPMFVBOHKUAUHPSLKPAAVAOLILUJOPADVBSKILWBZOPUNBWAOLKHPZPLZAOPZPZHUEALYTPUHS"

    plaintext = input("Enter the plaintext: ").upper()

    print("\nProcessing Encrypting with Caesar Cipher...")
    sleep(1)
    encryptedText = cipher.encrypt(plaintext)
    print("Encryption Completed!")
    print("Encrypted Text:", encryptedText)
    sleep(0.1)
    print("\nProcessing Decrypting with Caesar Cipher...")
    sleep(1)
    decryptedText = cipher.decrypt(encryptedText)
    print("Decryption Completed!")
    print("Decrypted Text:", decryptedText)

    sleep(0.5)
    print("\nCaesar Cipher Encryption and Decryption Completed!")
    sleep(0.5)

    sleep(1)
    print("\nPreparing for Brute Force Attack for the Ciphertext: " + ciphertext + "...")
    sleep(2)
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n--- Brute Force Attack ---\n")

    print("Ciphertext:", ciphertext)

    print("\nBrute Force Attack Results:")
    implementBruteForceAttack(ciphertext)

    sleep(0.5)
    print("\nBrute Force Attack Completed!")
    sleep(0.5)
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
