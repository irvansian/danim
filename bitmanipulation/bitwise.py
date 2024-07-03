def isEven(num):
    return num & 1 == 0


def isPowerOfTwo(num):
    return (num & (num - 1) == 0) and num > 0


def isBitKSet(num, k):
    return num & (1 << k) != 0


def toggleBitK(num, k):
    return num ^ (1 << k)


def setBitK(num, k):
    return num | (1 << k)


def unsetBitK(num, k):
    return num & ~(1 << k)


def toggleTwoValue(num):
    """
    if num == a:
        return b
    elif num == b:
        return a
    :param num:
    :return:
    """
    a = 10
    b = 20
    return a ^ b ^ num


def count_set_bits(num):
    setCount = 0

    while num:  # this unsets the right most 1 in the binary representation
        num &= (num - 1)
        setCount += 1

    return setCount
