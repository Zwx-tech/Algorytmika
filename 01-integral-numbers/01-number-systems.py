def decToAny(n: int, b: int) -> int:
    """
    :param n: dec num
    :param b: num system
    :return: converted num
    """
    response = ""
    while n > 0:
        d = n%b
        response += str(d) if d < 10 else chr(ord('A') + d - 10)
        n //= b
    response = response[::-1]
    return response


if __name__ == "__main__":
    n = [15, 12, 2, 4, 7, 8]
    print(decToAny(255, 16))
