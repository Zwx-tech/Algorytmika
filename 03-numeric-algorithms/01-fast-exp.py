def fastExp(base, exponent):
    if exponent == 0:
        return 1

    elif exponent % 2 == 0:
        # dla n prarzystego a^n = (a^(n/2))^2
        halfPower = fastExp(base, exponent // 2)
        return halfPower * halfPower

    # dla nie parzystego a^n = a * (a^(n-1))
    return base * fastExp(base, exponent - 1)
b = 2
e = 10
print(f"{b}^{e} = {fastExp(b, e)}")