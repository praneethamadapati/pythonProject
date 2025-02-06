def findPoisonedDuration(timeSeries, duration):

    if not timeSeries:
        return 0

    n = len(timeSeries)
    poisonedTime = 0

    for i in range(n-1):
        time = min(duration, timeSeries[i+1] - timeSeries[i])
        poisonedTime += time

    poisonedTime += duration
    return poisonedTime

print(findPoisonedDuration([1,2], 2))