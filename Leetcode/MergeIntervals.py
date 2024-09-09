def mergeIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    mergedResult = []

    for interval in intervals:
        if not mergedResult or mergedResult[-1][1] < interval[0]:
            mergedResult.append(interval)
        else:
            mergedResult[-1][1] = max(mergedResult[-1][1], interval[1])

    return mergedResult

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeIntervals(intervals))