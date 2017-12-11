from math import floor
coords = [('n', 0, 1, -1), ('s', 0, -1, 1), ('ne', 1, 0, -1), ('nw', -1, 1, 0), ('se', 1, -1, 0), ('sw', -1, 0, 1)]


def get_file_and_format():
    with open('day_11/input.txt') as f:
        return f.read()


def main(inputs):
    origin = (0, 0, 0)
    max_dist = 0
    for d in inputs:
        mvmt = list(filter(lambda coord: coord[0] == d, coords))[0]
        x0, y0, z0 = origin
        dir, x, y, z = mvmt

        origin = (x0 + x, y0 + y, z0 + z)
        curr_dist = dist((0, 0, 0), origin)
        if curr_dist > max_dist:
            max_dist = curr_dist
    return dist((0, 0, 0), origin), max_dist


def dist(p1, p2):
    y1, x1, z1 = p1
    y2, x2, z2 = p2
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return max(abs(dx), abs(dy), abs(dz))


i = get_file_and_format()
i = i.split(',')
print(i)
res = main(i)
print(res)