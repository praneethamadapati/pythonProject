def powerOfThree(n):
    if n <= 0:
        return False
    while n:
        if n == 1:
            return True
        elif n % 3 != 0:
            return False
        else:
            n = n / 3


n = 27
print(powerOfThree(n))