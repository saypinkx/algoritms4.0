n, m = map(lambda x: int(x), str(input()).split())

a = list(map(lambda x: int(x), str(input()).split()))


def not_min(l, r, a):
    elem = a[l]
    for i in range(l, r + 1):
        if a[i] > elem:
            return a[i]
        elif a[i] < elem:
            return elem
    return 'NOT FOUND'


for i in range(m):
    l, r = map(lambda x: int(x), str(input()).split())
    print(not_min(l, r, a))
