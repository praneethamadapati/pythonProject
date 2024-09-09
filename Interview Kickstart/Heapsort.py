def Heapsort(arr):
    arr.insert(0, -1)
    print(arr)
    n = len(arr)
    helperFunction(arr, n)

    arr.remove(-1)
def helperFunction(arr, n):

    i = n - 1
    while i > 1:
        parentIndex = i//2
        if arr[i] > arr[parentIndex]:
            arr[i], arr[parentIndex] = arr[parentIndex], arr[i]
            print(arr)

        printArray(arr)
        i -= 1
    print(arr)
    arr[1], arr[n-1] = arr[n-1], arr[1]
    n -= 1
    if n > 0:
        helperFunction(arr, n)

    # arr.pop(0)

def printArray(arr):
    n = len(arr)
    currentIndex = 1
    rows = 1
    while currentIndex < n:
        for i in range(rows):
            print(arr[currentIndex], end=" ")
            currentIndex += 1
        print()
        rows *= 2

def heapify(arr):
    n = len(arr)
    for i in range(1, n-1):
        child1 = i * 2
        child2 = (i * 2) + 1



arr = [6, 4, 3, 8, 1, 5, 2, 7, -1000, 205, 15 , 17 ,18,-306, 152]
print(arr)
Heapsort(arr)
print(arr)