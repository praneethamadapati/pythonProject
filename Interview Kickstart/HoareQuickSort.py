def HoareQuickSort(arr):
    n = len(arr)

    helperFunction(arr, 0, n-1)

def helperFunction(arr, start, end):
    if start >= end:
        return arr

    smaller = start + 1
    bigger = end

    while smaller <= bigger:
        if arr[smaller] < arr[start]:
            smaller += 1
        elif arr[bigger] > arr[start]:
            bigger -= 1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller += 1
            bigger -= 1
    arr[start], arr[bigger] = arr[bigger], arr[start]

    helperFunction(arr, start, bigger - 1)
    helperFunction(arr, bigger + 1, end)

arr = [6, 4, 3, 8, 1, 5, 2, 7, -102, 302, 102]
print(arr)
HoareQuickSort(arr)
print(arr)