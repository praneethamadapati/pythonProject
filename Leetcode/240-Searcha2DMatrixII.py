def searchA2DMatrixII(matrix, target):
    for row in matrix:
        if binarySearch(row, target):
            return True
    return False

def binarySearch(row, target):
    left = 0
    right = len(row) - 1
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == target:
            return True
        elif row[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
