def sqarerootofx(x):


    if x < 2:
        return x

    left, right = 2, x//2

    while left < right:
        mid = (left + right)//2
        numberSquare = mid * mid

        if mid == numberSquare:
            return mid
        elif numberSquare > x:
            right = mid - 1
        else:
            left = mid + 1

    return mid - 1 if numberSquare > x else mid

print(sqarerootofx(9))