def radixSort(arr):
    n = len(arr)
    maxElement = max(arr)
    digitLength = maxElementLength = len(str(maxElement))
    # maxElementLength = int(len(str(max(arr))))
    print(digitLength)
    # loop = 1
    resultArray = []
    # while loop <= maxElementLength:
    lowestDigit = 0
    while len(resultArray) <= n:
        for i in range(n-1):
            print(f'Number is: {arr[i]}')
            if arr[i] % 10 == lowestDigit:
                resultArray.append(arr[i])
                print(resultArray)
                arr.pop(i)
    lowestDigit += 1
    print(resultArray)
    return resultArray


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
