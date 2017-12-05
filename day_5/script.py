def get_file_and_format():
    with open('day_5/input.txt') as f:
        return [s.strip() for s in f.read().splitlines()]


class Walker:
    steps = 0
    the_end = False

    def __init__(self, lst):
        self.lst = [int(s) for s in lst]
        self.current_index = 0

    def main(self):
        try:
            while not self.the_end:
                self.step()

        except ValueError:
            self.the_end = True
        finally:
            return self.steps

    def main_2(self):
        try:
            while not self.the_end:
                self.step_2()

        except ValueError:
            self.the_end = True
        finally:
            return self.steps

    def step(self):
        val = self.lst[self.current_index]
        self.steps += 1
        self.lst[self.current_index] += 1
        self.current_index += val

    def step_2(self):
        val = self.lst[self.current_index]
        self.steps += 1
        if val >= 3:
            self.lst[self.current_index] -= 1
        else:
            self.lst[self.current_index] += 1
        self.current_index += val


w = Walker(get_file_and_format())
res = w.main_2()
print(res)