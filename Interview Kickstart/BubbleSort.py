def bubbleSort(arr):
    n = len(arr)
    for j in range(n):
        for i in range(n - 1, j, -1):
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr


arr = [6, 4, 3, 8, 1, 5, 2, 7]
print(arr)
bubbleSort(arr)
print(arr)