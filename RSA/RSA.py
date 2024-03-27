import random

class RSA:
    def __init__(self, bits):
        self.bits = bits

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_prime(self):
        while True:
            p = random.getrandbits(self.bits)
            if self.is_prime(p):
                return p

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def mod_inverse(self, a, m):
        gcd, x, y = self.extended_gcd(a, m)
        if gcd != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def keygen(self):
        p = self.generate_prime()
        q = self.generate_prime()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(2, phi - 1)
        while self.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        d = self.mod_inverse(e, phi)
        return (n, e), (n, d)

    def encrypt(self, plaintext, public_key):
        n, e = public_key
        return pow(plaintext, e, n)

    def decrypt(self, ciphertext, private_key):
        n, d = private_key
        return pow(ciphertext, d, n)

    def encrypt_string(self, plaintext, public_key):
        n, e = public_key
        return [pow(ord(char), e, n) for char in plaintext]

    def decrypt_string(self, ciphertext, private_key):
        n, d = private_key
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])

    def compute_time_complexity(self, n):
        return n ** 2

    def compute_space_complexity(self, n):
        return n

def main():
    plaintext = 8
    rsa = RSA(3)
    public_key, private_key = rsa.keygen()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    ciphertext = rsa.encrypt(plaintext, public_key)
    print("Encrypted Ciphertext:", ciphertext)

    decrypted_plaintext = rsa.decrypt(ciphertext, private_key)
    print("Decrypted Plaintext:", decrypted_plaintext)

    plaintext = "HELLO"
    rsa = RSA(3)
    public_key, private_key = rsa.keygen()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    ciphertext = rsa.encrypt_string(plaintext, public_key)
    print("Encrypted Ciphertext:", ciphertext)

    decrypted_plaintext = rsa.decrypt_string(ciphertext, private_key)
    print("Decrypted Plaintext:", decrypted_plaintext)

    n = 3
    print("Time Complexity:", rsa.compute_time_complexity(n))
    print("Space Complexity:", rsa.compute_space_complexity(n))


if __name__ == '__main__':
    main()