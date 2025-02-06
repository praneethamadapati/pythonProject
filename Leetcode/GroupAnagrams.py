from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)

    for str in strs:
        sorted_string = ''.join(sorted(str))
        result[sorted_string].append(str)
    # print(result)
    return list(result.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))