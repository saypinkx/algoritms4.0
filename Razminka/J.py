t = int(input())


def is_mod(n, a, b):
    old_n = n
    for i in range(b, a - 1, -1):
        b = i
        n = old_n
        while n % b > 0 and b != a:
            n = n % b
            b = b - 1
        if n % b == 0:
            return 'YES'
    return 'NO'


def is_del(n, a, b):
    for i in range(b, a - 1, -1):
        if n % i == 0:
            return True
    return False


def is_mod2(n, a, b):
    for i in range(b, a - 1, -1):
        new_n = n
        while new_n >= a:
            new_n = new_n - i
            if is_del(new_n, a, i) or new_n == 0:
                return 'YES'
    return 'NO'


def is_mod3(n, a, b):
    if n % a == 0 or n % b == 0:
        return 'YES'
    if a * (n // a) <= n and b * (n // a) >= n:
        return 'YES'
    return 'NO'


for i in range(t):
    n, a, b = list(map(lambda x: int(x), str(input()).split()))
    print(is_mod3(n, a, b))
