def isEven(num):
    return num & 1 == 0


def isPowerOfTwo(num):
    return (num & (num - 1) == 0) and num > 0

