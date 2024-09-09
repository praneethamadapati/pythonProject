def countingSort(arr):
    maxElement = max(arr)
    minElement = min(arr)
    totalElements = maxElement - minElement + 1

    countingArray = [0]*(totalElements)
    for number in arr:
        # print(f'Number is: {number}')
        currentIndex = number - minElement
        # print(countingArray[currentIndex])
        if countingArray[currentIndex] != 0:
            countingArray[currentIndex] += 1
        else:
            countingArray[currentIndex] = 1
    # print(f'CountingArray is: {countingArray}')

    resultArray = []
    n = len(countingArray)
    for index, number in enumerate(countingArray):
        currentNumber = index+minElement
        i = 1
        while i <= number:
            resultArray.append(currentNumber)
            i += 1
    # print(f'CountingArray is: {resultArray}')
    return resultArray


    # elementCount = {}
    #
    # for number in arr:
    #     if number in elementCount:
    #         elementCount[number] += 1
    #     else:
    #         elementCount[number] = 1
    #
    # return elementCount

arr = [5, 8, 3, 9, 4, 1, 7, 7, -8]
print(countingSort(arr))