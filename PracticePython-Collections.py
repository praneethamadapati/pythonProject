import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

result = collections.ChainMap(dict1, dict2)
print(result.maps)

print('Keys: {}'.format(list(result.keys())))
print('Values: {}'.format(list(result.values())))

print('Elements: ')

for key, value in result.items():
    print('{}: {}'.format(key, value))


print('Day10 in result? {}'.format('day10' in result))

result2 = collections.ChainMap(dict2, dict1)
print(result.maps)
print(result2.maps)

dict1['day5'] = 'Sun'
print(result.maps)
print(result2.maps)