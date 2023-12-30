def bucketing(mass, i):
    bucket = dict()
    for j in range(len(mass)):
        if mass[j][i] not in bucket:
            bucket[mass[j][i]] = [mass[j]]
        else:
            bucket[mass[j][i]].append(mass[j])
    result = []
    for i in range(0, 10):
        i = str(i)
        if i in bucket:
            print(f'Bucket {i}: {", ".join(bucket[i])}')
            for elem in bucket[i]:
                result.append(elem)
        else:
            print(f'Bucket {i}: empty')
    return result


def bitwise_sort(mass, n):
    bits = len(mass[0])
    print('Initial array:')
    print(*mass, sep=', ')
    print('*' * 10)
    for i in range(bits):
        bit = bits - 1 - i
        print(f'Phase {i + 1}')
        mass = bucketing(mass, bit)
        print('*' * 10)
    return mass

n = int(input())
mass = []
for i in range(n):
    mass.append(input())

result = bitwise_sort(mass, n)

print(f'Sorted array:')
print(*result, sep=', ')
