def is_equal(l, a, b):
    l, a, b = l, a, b
    a += 1
    b += 1
    hash_b = (h_rev[b + l - 1] - h_rev[b - 1] * mass_x[l]) % p
    hash_a = (h[a + l - 1] - h[a - 1] * mass_x[l]) % p
    if hash_a == hash_b:
        return 1
    return 0


s = str(input())
n = len(s)
s_rev = s[::-1]

h = [0] * (n + 1)
h_rev = [0] * (n + 1)

mass_x = [1] * (n + 1)
x = 257
p = 10 ** 9 + 7
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x + ord(s[i - 1])) % p
    h_rev[i] = (h_rev[i - 1] * x + ord(s_rev[i - 1])) % p
    mass_x[i] = (mass_x[i - 1] * x) % p

# def is_reverse():
# #
# count = 0
# for i in range(0, n):
#     for j in range(1, n - i + 1):
#         if is_equal(j, i, n - j - i):
#             count += 1
#     left = 0
#     right = n - i + 1
#     while left != right:
#
# print(count)
count = 0
n = n - 1
for i in range(0, n):
    left = 0
    right = (i + 1) * 2
    while left != right:
        m = (left + right + 1) // 2
        if m % 2 == 0:
            if m // 2 == 0 or is_equal(m // 2, i + 1 - m // 2, n - m // 2 - i):
                left = m
            else:
                right = m - 1
        elif m % 2 != 0:

            if m // 2 == 0 or is_equal(m // 2 + 1, i - m // 2 - 1, n - m // 2 - i - 1):
                left = m
            else:
                right = m - 1
    if left % 2 == 0:
        count += left // 2 + 1
    else:
        count += left // 2
print(count)
