def isPerfectNumber(n: int) -> bool:
    """
    Function checks if n is a perfect number
    :param n: number that we want to check
    :return: true/false
    """
    s = 1 + sum([
        i for i in range(2, n) if n % i == 0
    ])
    return n == s and n != 1

print(isPerfectNumber(496))
