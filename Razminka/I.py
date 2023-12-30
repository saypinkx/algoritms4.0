class Stack:
    def __init__(self):
        self.head: StackObj = None

    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            old_node: StackObj = self.head
            node.next = old_node
            self.head = node

    def remove(self):
        self.head = self.head.next

    def __len__(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length


class StackObj:
    def __init__(self, value):
        self.next = None
        self.value = value


string = str(input())


def is_true(stack: Stack, string):
    for i in range(0, len(string)):
        simvol = string[i]
        if stack.head is None:
            stack.add(StackObj(simvol))
        else:
            simvol_stack = stack.head.value
            if simvol == ')' and simvol_stack == '(':
                stack.remove()
            elif simvol == ']' and simvol_stack == '[':
                stack.remove()
            elif simvol == '}' and simvol_stack == '{':
                stack.remove()
            else:
                stack.add(StackObj(simvol))

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'


print(is_true(stack=Stack(), string=string))