def countPrimes(n):
    if n < 2:
        return 0
    result = [True]*n
    # result[0], result[1] = False
    m = 2
    while m * m < n:
        if result[m]:
            for j in range(m * m, n, m):
                result[j] = False
        m += 1
    print(result)
    prime_numbers = []
    for i in range(2, len(result)):
        if result[i] == True:
            prime_numbers.append(i)
    print(prime_numbers)
    return result.count(True) - 2


print(countPrimes(10))
