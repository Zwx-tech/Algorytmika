def decToAny(n: int, b: int) -> int:
    """
    :param n: dec num
    :param b: num system
    :return: converted num
    """
    response = ""
    while n > 0:
        d = n % b
        response += str(d) if d < 10 else chr(ord('A') + d - 10)
        n //= b
    response = response[::-1]
    return response


if __name__ == "__main__":
    n = [255, 256, 20, 40, 70, 80]
    for i in n:
        print(decToAny(i, 16))
