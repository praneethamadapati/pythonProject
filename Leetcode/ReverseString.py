def reverseString(s):
    for index in range(len(s)//2):
        s[index], s[len(s)-1-index] = s[len(s)-1-index], s[index]
    return s

s = ["h", "e", "l", "l", "o"]
print(reverseString(s))