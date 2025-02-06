def longestSubstringWithoutRepeatingCharacters(s):
    char_dict = {}
    left = 0
    maximum_length = 0

    for right in range(len(s)):
        character = s[right]
        if character in char_dict and char_dict[character] >= left:
            left = char_dict[character] + 1
        # if character not in char_dict:
        #     result += result.join(character)

        char_dict[character] = right

        maximum_length = max(maximum_length, right - left + 1)
    # print(result)
    return maximum_length

    # dict = {}
    # maximumLength = 0
    # left = 0
    # for right in range(len(s)):
    #     character = s[right]
    #     if character in dict and dict[character] >= left:
    #         left = dict[character] + 1
    #
    #     dict[character] = right
    #     maximumLength = max(maximumLength, right - left + 1)
    #
    # return maximumLength

s = "pwwkew"
print(longestSubstringWithoutRepeatingCharacters(s))