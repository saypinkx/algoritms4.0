def is_equal(l, a, b):
    l, a, b = l, a, b
    a += 1
    b += 1
    hash_b = (h[b + l - 1] - h[b - 1] * mass_x[l]) % p
    hash_a = (h[a + l - 1] - h[a - 1] * mass_x[l]) % p
    if hash_a == hash_b:
        return 1
    return 0


s = str(input())
n = len(s)
h = [0] * (n + 1)
mass_x = [1] * (n + 1)
x = 257
p = 10 ** 9 + 7
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    mass_x[i] = (mass_x[i - 1] * x) % p

maxes = 0
result = len(s)
for i in range(1, n):
    left, right = 0, n - i
    while left < right:
        m = (left + right + 1) // 2
        if is_equal(m, 0, i):
            left = m
        else:
            right = m - 1
    if left >= maxes and i + left == n:
        maxes = left
        result = i

print(result)
