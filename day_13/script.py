import itertools


def get_file_and_format():
    with open('day_13/input.txt') as f:
        return parse(f.read())


def parse(f):
    return [line.split(': ') for line in f.splitlines()]


class Scanner:

    def __init__(self, l=get_file_and_format()):
        self.lines = l
        self.heights = {int(pos): int(height) for pos, height in self.lines}

    def scan(self, height, time):
        offset = time % ((height - 1) * 2)

        return 2 * (height - 1) - offset if offset > height - 1 else offset

    def main(self):
        return sum(pos * self.heights[pos] for pos in self.heights if self.scan(self.heights[pos], pos) == 0)

    def main_2(self):
        return next(wait for wait in itertools.count() if not any(self.scan(self.heights[pos], wait + pos) == 0 for pos in self.heights))


if __name__ == '__main__':
    scanner = Scanner()
    print('Part 1 answer: ', scanner.main())
    print('Part 2 answer: ', scanner.main_2())
