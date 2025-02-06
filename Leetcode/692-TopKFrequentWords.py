from collections import Counter


def topKFrequentWords(words, k):
    dict = Counter(words)
    result = []
    # for word in words:
    #     if word in dict:
    #         dict[word] += 1
    #     else:
    #         dict[word] = 1
    # return [key for key, val in dict.items() if val == k]
    sorted_dict = sorted(dict.items(), key = lambda item: (-item[1], item[0]))
    print(sorted_dict)
    for key, value in sorted_dict:
        if k > 0:
            result.append(key)
        k -= 1
    return result

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 2
print(topKFrequentWords(words, k))