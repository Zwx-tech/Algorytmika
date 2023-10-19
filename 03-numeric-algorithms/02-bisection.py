E = 0.00001
def f(x):
    return x**3 - x**2 + 2 # -1
def bisection(a, b, max_interation):
    for k in range(1, max_interation):
        x = (a + b) / 2
        if abs(f(x)) < E:
            return x
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x
    return x

print(bisection(-3, 1, 1000))