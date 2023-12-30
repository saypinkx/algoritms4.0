def create_fraction(a, b, c, d):
    numerator = a * d + c * b
    denominator = b * d
    if numerator >= denominator:
        for i in range(denominator, 0, -1):
            if numerator % i == 0 and denominator % i == 0:
                return numerator // i, denominator // i
    else:
        for i in range(numerator, 0, -1):
            if numerator % i == 0 and denominator % i == 0:
                return numerator // i, denominator // i


a, b, c, d = map(lambda x: int(x), str(input()).split())

print(*create_fraction(a, b, c, d))
