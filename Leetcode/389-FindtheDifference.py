def findTheDifference(s, t):
    extra_character = ''
    t_ascii = 0
    s_ascii = 0
    print(ord('P'))
    print(chr(80))
    for char_t in t:
        t_ascii += ord(char_t)
    for char_s in s:
        s_ascii += ord(char_s)

    return chr(t_ascii - s_ascii)

s = "abcd"
t = "abcde"
print(findTheDifference(s, t))