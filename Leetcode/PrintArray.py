def printArray(arr):
    n = len(arr)
    currentIndex = 0
    rows = 1
    while currentIndex < n:
        for i in range(rows):
            print(arr[currentIndex], end=" ")
            currentIndex += 1
        print()
        rows *= 2


arr = [6, 4, 3, 8, 1, 5, 2, 7, -1000, 205, 15, 17, 18, -306, 152]
print(arr)
printArray(arr)
