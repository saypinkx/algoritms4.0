k = int(input())
n = int(input())
humans = []
for i in range(n):
    a = int(input())
    humans.append(a)
humans = humans[::-1]
i = 0
counter = k
time = 0
while i <= n - 1:
    if humans[i] == 0:
        i += 1
    elif humans[i] - counter > 0:
        n_time = humans[i] // counter
        humans[i] = humans[i] - counter * n_time
        time += (n - i) * 2 * n_time
    elif humans[i] - counter < 0:
        j = i + 1
        dop = counter - humans[i]
        while j <= n - 1 and dop != 0:
            if humans[j] == 0:
                j = j + 1
            elif humans[j] - dop >= 0:
                humans[j] -= dop
                dop = 0
            elif humans[j] - dop < 0:
                dop = dop - humans[j]
                j = j + 1
        time += (n - i) * 2
        i = j
    elif humans[i] - counter == 0:
        time += (n - i) * 2
        i = i + 1
print(time)

#
# class Stack:
#
#     def __init__(self):
#         self.head = None
#
#     def add(self, node):
#         if self.head is None:
#             self.head = node
#         else:
#             new_head = node
#             self.head =
#
#
# class StackObj:
#     def __init__(self):
#         self.next = None
