def selectionSort(arr):
    n = len(arr)

    for j in range(n):
        min_value = arr[j]
        low=j
        for i in range(j+1, n):
            if min_value > arr[i]:
                low = i
                min_value = arr[low]

        arr[low], arr[j] = arr[j], arr[low]
        print(arr)
    return arr


for i in range(len(arr)):
        minIn = i
        for j in range(i+1,len(arr)):
            if arr[minIn] > arr [j]:
                minIn = j
        arr[i], arr[minIn] = arr[minIn], arr[i]

arr = int(input("Enter an array: "))
# arr = [6, 4, 3, 8, 1, 5, 2, 7]
# print(arr)
selectionSort(arr)
# print(arr)
# [6, 4, 3, 8, 1, 5, 2, 7]