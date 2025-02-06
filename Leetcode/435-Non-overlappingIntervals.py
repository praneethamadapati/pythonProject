def nonOverlappingIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key = lambda x:x[1])
    counter = 0
    end = float('-inf')

    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            counter += 1
    return counter


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(nonOverlappingIntervals(intervals))