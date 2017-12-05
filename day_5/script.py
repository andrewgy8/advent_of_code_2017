def get_file_and_format():
    with open('day_5/input.txt') as f:
        return [s.strip() for s in f.read().splitlines()]


class Walker:
    steps = 0
    the_end = False

    def __init__(self, lst, part_two=False):
        self.part_two = part_two
        self.lst = [int(s) for s in lst]
        self.index = 0

    def main(self):
        try:
            while not self.the_end:
                self.step()
        except ValueError:
            self.the_end = True
        finally:
            return self.steps

    def step(self):
        val = self.lst[self.index]
        self.steps += 1
        if self.part_two and val >= 3:
            self.lst[self.index] -= 1
        else:
            self.lst[self.index] += 1
        self.index += val
