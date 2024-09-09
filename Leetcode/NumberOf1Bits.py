def numberOfOneBits(num):
    convertToBinary(num)
    # num = bin(num)
    # num = str(num)
    # count = num.count('1')
    # print(count)


def convertToBinary(num):
    binary = []
    while num > 1:
        num, remainder = divmod(num, 2)
        binary.append(remainder)
    binary.append(num)
    # print(num)
    # print(binary)
    binary.reverse()
    # print(binary)
n = 11
numberOfOneBits(n)
