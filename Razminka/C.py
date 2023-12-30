from math import atan, pi, radians, degrees, atan2


def get_degree(x, y):
    if x == 0:
        if y > 0:
            return degrees(pi / 2)
        if y < 0:
            return degrees(pi / 2 * 3)
        if y == 0:
            return 'error'
    elif y == 0:
        if x > 0:
            return degrees(0)
        else:
            return degrees(pi)

    else:
        return degrees(atan2(y, x))
    # if x > 0 and y > 0:
    #     return degrees(atan(y/ x))
    # if x < 0 and y > 0:
    #     return degrees(pi / 2 + abs(atan(y/ x)))
    # if x > 0 and y < 0:
    #     return degrees(pi * 2 - abs(atan(y/ x)))
    # if x < 0 and y < 0:
    #     return degrees(pi / 2 * 3 - abs(atan(y/ x)))

#
# def min_distance(xa, ya, xb, yb):
#     ra = (xa * xa + ya * ya) ** 0.5
#     rb = (xb * xb + yb * yb) ** 0.5
#     a = get_degree(xa, ya)
#     b = get_degree(xb, yb)
#     if a == 'error' or b == 'error':
#         return max(ra, rb)
#     distance_two_line = ra + rb
#     distance_line_okr_1 = abs(ra - rb) + pi * rb / degrees(pi) * (degrees(pi * 2) - abs(a - b))
#     distance_okr_line_1 = pi * ra / degrees(pi) * (degrees(pi * 2) - abs(a - b)) + abs(ra - rb)
#     distance_line_okr_2 = abs(ra - rb) + pi * rb / degrees(pi) * abs(a - b)
#     distance_okr_line_2 = pi * ra / degrees(pi) * abs(b - a) + abs(ra - rb)
#     return min(distance_two_line, distance_line_okr_1, distance_okr_line_2, distance_line_okr_2, distance_okr_line_1)


def min_distance2(xa, ya, xb, yb):
    ra = (xa * xa + ya * ya) ** 0.5
    rb = (xb * xb + yb * yb) ** 0.5
    a = get_degree(xa, ya)
    b = get_degree(xb, yb)
    if a == 'error' or b == 'error':
        return max(ra, rb)
    distance_two_line = ra + rb
    if a - b <= degrees(180):
        distance_line_okr = abs(ra - rb) + pi * min(ra, rb) / degrees(pi) * abs(a - b)
    else:
        distance_line_okr = abs(ra - rb) + pi * min(ra, rb) / degrees(pi) * (degrees(pi * 2) - abs(a - b))
    return min(distance_two_line, distance_line_okr)


xa, ya, xb, yb = map(lambda x: int(x), str(input()).split())
print(min_distance2(xa, ya, xb, yb))

# -444444 -333333 888888 666666
