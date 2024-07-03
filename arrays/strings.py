def stringMatch(pattern, string):
    for i in range(len(string)):
        if string[i] != pattern[0]:
            continue

        j = i
        k = 0

        while k < len(pattern):
            if string[j] != pattern[k]:
                break
            j += 1
            k += 1

        if k == len(pattern):
            return i

    return -1


def allSubstring(s):
    results = []

    for i in range(len(s)):
        curString = ''
        for j in range(i, len(s)):
            curString += s[j]
            results.append(curString)

    return results