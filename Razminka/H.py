a = int(input())
b = int(input())
n = int(input())


def is_studentsA_gt_studentsB(a, b, n):
    max_students_a = a
    if b % n != 0:
        min_students_b = b // n + 1
    else:
        min_students_b = b // n

    if max_students_a > min_students_b:
        return 'Yes'
    else:
        return 'No'


print(is_studentsA_gt_studentsB(a, b, n))
