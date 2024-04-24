import time

def binaryComparison(binaryText1, binaryText2):
    if len(binaryText1) != len(binaryText2):
        return "The binary texts are not of the same length."
    identicalBits = 0
    for i in range(len(binaryText1)):
        if binaryText1[i] == binaryText2[i]:
            identicalBits += 1
    return identicalBits

def main():
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n--- Binary Comparison ---\n")

    binaryText1 = "0110010110010101101010000100111010100101101010001101110000011011100101001111110011110001001111111010000101011010100111000100101100101001110100010000100000110010100001010000111001001110101011100100101111010001111010010011100110101010000101101111111111001010"
    binaryText2 = "0110101011001110000010100001000101100101000100100110011111100110100010011101110101000000101000011001010100101001011001100100101001011000110000011011011000110101110000010100101100111010001010100000001111100110100011111111001110010010010110101000110000011010"
    print("Binary Text 1:", binaryText1)
    print("Binary Text 2:", binaryText2)
    print("\nLength of Binary Text 1:", len(binaryText1))
    print("Length of Binary Text 2:", len(binaryText2))

    print("\nComparing the binary texts...\n")
    time.sleep(0.1)
    print("Identical bits:", binaryComparison(binaryText1, binaryText2))

    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()