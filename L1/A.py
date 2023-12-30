


def partition(n, mass, pivot):
    eq, gr, nw = 0, 0, 0
    while nw != n:
        if mass[nw] == pivot:
            mass[gr], mass[nw] = mass[nw], mass[gr]
            gr += 1
        elif mass[nw] < pivot:
            if gr == eq or nw == gr:
                mass[eq], mass[nw] = mass[nw], mass[eq]
            else:
                mass[eq], mass[gr], mass[nw] = mass[nw], mass[eq], mass[gr]
            eq += 1
            gr += 1
        nw += 1
    print(mass)
    return eq, n - eq


n = int(input())
string = str(input()).split()
mass = list(map(lambda x: int(x), string))
pivot = int(input())
z = partition(n, mass, pivot)
print(z[0], z[1], sep='\n')
