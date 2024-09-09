def reverseBits(n, length):
    binaryString = bin(n)[2:]
    print(binaryString)
    binaryString = binaryString.zfill(length)
    print(binaryString)
    reversedBinaryString = binaryString[::-1]
    print(reversedBinaryString)
    # reversedBinaryString = reversedBinaryString.zfill(length)
    binaryArray = [int(digit) for digit in reversedBinaryString]
    print(binaryArray)

    # n[:] = n[::-1]
    # print(n[::-1])
    # print(len(n[::-1]))
    # digits = [n]
    # print(digits)
    decimalNumber = int(reversedBinaryString, 2)
    # power = len(binaryArray) - 1
    # for i in range(len(binaryArray)):
    #     # print(n[i])
    #     # print(2**i)
    #     decimalNumber += int(binaryArray[i]*2**power)
    #     power -= 1
    #     # print(decimalNumber)
    return decimalNumber

n = 0b000000010100101000001111010011100
length = 32
print(reverseBits(n, length))