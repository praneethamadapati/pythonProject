def happyNumber(n):

    count = 1
    while count <= 10:
        arr = numberToArray(n)
        squaredSum = squaredNumber(arr)
        count += 1
        print(count, squaredSum)
        if squaredSum == 1:
            return True
        n = squaredSum
    return False

def squaredNumber(arr):
    squaredSum = 0
    for number in arr:
        squaredSum += number * number
    return squaredSum
# n = sum(digit**2 for digit in digits)
def numberToArray(num):
    arr = []
    while num > 0:
        arr.append(num % 10)
        num = num // 10
    return arr
# digits = [int(digit) for digit in str(n)]
n = 2
print(happyNumber(n))
