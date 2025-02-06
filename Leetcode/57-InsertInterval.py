def insertInterval(intervals, newInterval):
    # result = []
    # for interval in intervals:
    #     if interval[0] < newInterval[0] and newInterval not in result:
    #         result.append(interval)
    #     elif interval[0] > newInterval[0] and newInterval not in result:
    #         result.append(newInterval)
    #         result.append(interval)
    #     else:
    #         result.append(interval)
    #
    #
    # return result

    result = []

    newStart, newEnd = newInterval[0], newInterval[1]
    i, n = 0, len(intervals)

    while i < n and intervals[i][1] < newStart:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newEnd:
        newStart = min(intervals[i][0], newStart)
        newEnd = max(intervals[i][1], newEnd)
        i += 1
    result.append([newStart, newEnd])

    while i < n:
        result.append(intervals[i])
        i += 1

    return result

intervals = [[1, 2], [6, 9]]
newInterval = [3, 5]
print(insertInterval(intervals, newInterval))