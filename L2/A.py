

s = str(input())
n = len(s)
h = [0] * (n + 1)
mass_x = [1] * (n + 1)
x = 10
p = 10 ** 9 + 7
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    mass_x[i] = (mass_x[i - 1] * x) % p

m = int(input())
for i in range(m):
    l, a, b = list(map(lambda x: int(x), input().split()))
    a += 1
    b += 1
    hash_b = (h[b + l - 1] - h[b - 1] * mass_x[l]) % p
    hash_a = (h[a + l - 1] - h[a - 1] * mass_x[l]) % p
    if hash_a == hash_b:
        print('yes')
    else:
        print('no')
