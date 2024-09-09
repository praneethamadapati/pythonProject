def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr


arr = [6, 4, 3, 8, 1, 5, 2, 7]
print(arr)
insertionSort(arr)
print(arr)
