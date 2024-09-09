def firstUniqueCharacterInString(s):
    result = {}
    for character in s:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    for index in range(len(s)):
        if result[s[index]] == 1:
            return index
    return -1


s = "loveleetcode"
print(firstUniqueCharacterInString(s))
