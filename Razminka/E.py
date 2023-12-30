n = int(input())
a = list(map(lambda x: int(x), str(input()).split()))


def prefix2(n, a):
    result = []
    prefix_sum = []
    summa = 0
    prefix_sum.append(summa)
    for j in range(n):
        summa += a[j]
        prefix_sum.append(summa)
    for i in range(n):
        sum1 = prefix_sum[n] - prefix_sum[i] - a[i] * (n - i) + a[i] * i - prefix_sum[i]
        result.append(sum1)
    return result


print(*prefix2(n, a))
