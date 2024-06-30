def rotate_array(array, k):
    """
    TWO POINTERS:
    1. reverse the array
    2. reverse the array [0:k - 1]
    3. reverse the array [k:]

    time = O(n), space = O(1)
    """

    def rev(l, r):
        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1

    rev(0, len(array) - 1)
    rev(0, k - 1)
    rev(k, len(array) - 1)

    return array


def reverse_array(array):
    """
    TWO POINTERS (original; same speed)
    :param array:
    :return:
    """
    l, r = 0, len(array) - 1

    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1

    return array


def reverse_vowels(s):
    """
    TWO POINTERS (move ptr under a condition; different speed)
    Use two whiles inside a while.
    :param s:
    :return:
    """
    s = list(s)
    vowels = 'aiueoAIUEO'
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not s[l] in vowels:
            l += 1

        while l < r and not s[r] in vowels:
            r -= 1

        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return ''.join(s)


def plant_flower(flowerbeds, n):
    """
    GREEDY
    optimal solution in substructure leads to optimal solution overall
    :param flowerbeds:
    :param n:
    :return:
    """
    if flowerbeds[0] == 0 and (len(flowerbeds) == 1 or flowerbeds[1] == 0):
        flowerbeds[0] = 1
        n -= 1

    for i in range(1, len(flowerbeds) - 1):
        if flowerbeds[i] == 1:
            continue

        if flowerbeds[i - 1] == 0 and flowerbeds[i + 1] == 0:
            flowerbeds[i] = 1
            n -= 1

    if flowerbeds[-1] == 0 and flowerbeds[-2] == 0:
        flowerbeds[-1] = 1
        n -= 1

    return n <= 1


def compress_inplace(chars):
    """
    TWO POINTERS (read & write pointer)
    :param chars:
    :return:
    """
    if not chars:
        return 0

    write = 0
    cur_char = chars[0]
    char_count = 0

    for char in chars:
        if char == cur_char:
            char_count += 1
            continue

        chars[write] = cur_char
        write += 1

        if char_count > 1:
            for digit in str(char_count):
                chars[write] = digit
                write += 1

        cur_char = char
        char_count = 1

    chars[write] = cur_char
    write += 1

    if char_count > 1:
        for digit in str(char_count):
            chars[write] = digit
            write += 1

    return write
