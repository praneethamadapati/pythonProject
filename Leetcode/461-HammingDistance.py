def hammingDistance(x, y):
    binary_x = format(x, '032b')
    binary_y = format(y, '032b')
    print(f'binary_x', binary_x)
    print(f'binary_y', binary_y)
    count = 0
    for i in range(len(binary_x)):
        if binary_x[i] != binary_y[i]:
            count += 1
        else:
            continue
    return count

x = 1
y = 4
print(hammingDistance(x, y))