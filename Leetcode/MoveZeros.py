def moveZeros(arr):
    zeroIndex = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[zeroIndex] = arr[zeroIndex], arr[i]
            zeroIndex += 1
    return arr

nums = [0, 1, 0, 3, 12]
print(moveZeros(nums))