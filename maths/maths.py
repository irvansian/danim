def gcd(a, b):
    """
    equation : num1 = num2.x + remainder
    swapping a with b and b with a % b
    stops if the remainder is 0
    if an is smaller than b, the first iteration is swapping
    """

    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    lcm = (a * b)/gcd(a,b)
    """

    return (a * b) / gcd(a, b)
