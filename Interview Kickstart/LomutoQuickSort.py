def LomutoQuickSort(arr):

    n = len(arr)
    helperFunction(arr, 0, n-1)

def helperFunction(arr, start, end):
    if start >= end:
        return arr

    smaller = start
    for bigger in range(start+1, end+1):
        if arr[bigger] < arr[start]:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    arr[start], arr[smaller] = arr[smaller], arr[start]

    helperFunction(arr, start, smaller-1)
    helperFunction(arr, smaller+1, end)

arr = [6, 4, 3, 8, 1, 5, 2, 7, -102, 302, -210, 102]
print(arr)
LomutoQuickSort(arr)
print(arr)