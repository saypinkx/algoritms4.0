from random import randint


def partition(l, r, mass, pivot):
    eq, gr, nw, n = l, l, l, r
    while nw != n:
        if mass[nw] < pivot:
            if gr == eq or nw == gr:
                mass[eq], mass[nw] = mass[nw], mass[eq]
            else:
                mass[eq], mass[gr], mass[nw] = mass[nw], mass[eq], mass[gr]
            eq += 1
            gr += 1
        elif mass[nw] == pivot:
            mass[gr], mass[nw] = mass[nw], mass[gr]
            gr += 1

        nw += 1
    return eq, gr


def quicksort(l, r, mass):
    if r - l > 0:
        if r - l < 10:
            mass[l:r] = sorted(mass[l:r])
        else:
            pivot = mass[randint(l, r - 1)]
            eq, gr = partition(l, r, mass, pivot)
            quicksort(l, eq, mass)
            quicksort(gr, r, mass)


n = int(input())
string = str(input()).split()
mass = list(map(lambda x: int(x), string))
quicksort(0, n, mass)
print(*mass)
