def karatsuba(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = int(n//2)
    x1 = int(x // 10 ** half)
    x0 = int(x % 10 ** half)
    y1 = int(y // 10 ** half)
    y0 = int(y % 10 ** half)
    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba((x0 + x1), (y0 + y1)) - z0 - z2
    z = z2 * (10**n) + z1 * (10 ** half) + z0
    return z


print(karatsuba(5678, 1234))