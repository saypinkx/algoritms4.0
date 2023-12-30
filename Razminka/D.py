string1 = str(input())
string2 = str(input())


def is_anogram(string1, string2):
    if len(string1) != len(string2):
        return 'NO'
    else:
        string1 = sorted(string1)
        string2 = sorted(string2)
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                return 'NO'
        return 'YES'


print(is_anogram(string1, string2))
