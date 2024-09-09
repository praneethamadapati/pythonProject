def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    array1 = arr[0:mid]
    array2 = arr[mid:]
    mergeSort(array1)
    mergeSort(array2)
    i = 0
    j = 0
    k = 0
    while i < len(array1) or j < len(array2):
        if i == len(array1):
            arr[k] = array2[j]
            j += 1
        elif j == len(array2):
            arr[k] = array1[i]
            i += 1
        elif array1[i] <= array2[j]:
            arr[k] = array1[i]
            i += 1
        else:
            arr[k] = array2[j]
            j += 1
        k += 1


arr = [6, 4, 3, 8, 1, 5, 2, 7, -19, 5, -1023, 103]
print(arr)
mergeSort(arr)
print(arr)
