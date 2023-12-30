def merge(n, m, list1, list2):
    i, j = 0, 0
    list3 = []
    while i != n and j != m:
        if list1[i] > list2[j]:
            list3.append(list2[j])
            j += 1
        elif list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list1[i])
            list3.append(list1[i])
            i += 1
            j += 1
    list3.extend(list1[i:n])
    list3.extend(list2[j:m])
    return list3


def mergesort(n, mass):
    median = len(mass) // 2
    if median == 0:
        return mass
    left = mergesort(median, mass[0:median])
    right = mergesort(n-median, mass[median:n])
    result = merge(len(left), len(right), left, right)
    return result


n = int(input())
mass = list(map(lambda x: int(x), input().split()))
print(mergesort(n, mass))
