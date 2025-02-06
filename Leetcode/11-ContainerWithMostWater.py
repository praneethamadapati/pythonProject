def containerWithMostWater(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        max_water = max(max_water, (right - left) * min(height[left], height[right]))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(containerWithMostWater(height))


def containerWithMostWater2(height):
    left = 0
    right = len(height) - 1
    maximumWater = 0

    while left < right:
        maximumWater = max(maximumWater, (right - left) * min(height[left], height[right]))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximumWater

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(containerWithMostWater2(height))