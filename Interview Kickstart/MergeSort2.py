def mergeSort2(arr):
    n = len(arr)-1
    merge(arr, 0, n)
    return arr

def merge(arr, start, end):
    if start == end:
        return arr

    mid = (start + end)//2
    merge(arr, start, mid)
    merge(arr, mid+1, end)

    result = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            # print('Step-1 {}'.format(result))
            i += 1
        else:
            result.append(arr[j])
            # print('Step-2 {}'.format(result))
            j += 1
    while i <= mid:
        result.append(arr[i])
        # print('Step-3 {}'.format(result))
        i += 1
    while j <= end:
        result.append(arr[j])
        # print('Step-4 {}'.format(result))
        j += 1

    print('Result is {}'.format(result))
    m = 0

    for k in range(start, end+1):
        arr[k] = result[m]
        m += 1
    return arr

arr = [6, 4, 3, 8, 1, 5, 2, 7]
print(arr)
mergeSort2(arr)
print(arr)
