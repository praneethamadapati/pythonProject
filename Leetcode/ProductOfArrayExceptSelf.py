def productOfArrayExceptSelf(arr):
    n = len(arr)
    result = []
    maximumProduct = 1
    for i in range(n):
        maximumProduct = maximumProduct * arr[i]
        # print(f'Maximum Product: {maximumProduct} and i is: {i}')
        j = i + 1
        while arr[i] != 1 and j <= n - 1:
            product = arr[i] * arr[j]
            result.append(product)
            j += 1
    result.append(maximumProduct)
    return result


arr = [1, 2, 3, 4]
print(productOfArrayExceptSelf(arr))
