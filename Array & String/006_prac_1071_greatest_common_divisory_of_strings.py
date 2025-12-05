def switchwords(word1, word2):
    result = []

    for a,b in zip(word1, word2):
        result.append(a)
        result.append(b)

    mid = len(result) //2

    result.append(word2[mid:])
    result.append(word1[mid:])

    return ''.join(result)