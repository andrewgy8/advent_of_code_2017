from math import sqrt, ceil


def main(n):
    root = ceil(sqrt(n))
    odd_square = root if root % 2 != 0 else root + 1
    arm = (odd_square-1)/2
    cycle = n - ((odd_square-2)**2)
    offset = cycle % (odd_square-1)
    return arm + abs(offset-arm)

coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]


def main_2(n):
    x = y = dx = 0
    dy = -1
    grid = dict()
    origin = (0, 0)

    while True:
        total = 0

        for mvmt in coords:
            x0, y0 = mvmt
            curr_pos = (x0+x, y0+y)
            if curr_pos in grid:
                total += grid[curr_pos]
            # print(total)
            # print(n)

        if total > n:
            return total

        if (x, y) == origin:
            grid[origin] = 1
        else:
            grid[(x, y)] = total

        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
