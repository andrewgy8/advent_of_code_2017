class SpinLock:
    def __init__(self, steps):
        self.steps = steps
        self.state = [0]
        self.curr_index = 0

    def loop(self):
        for i in range(1, 2018):
            pos = (self.curr_index + self.steps) % len(self.state)
            self.state.insert(pos + 1, i)
            self.curr_index = pos + 1

    def loop2(self):
        n = 0
        for i in range(1, 50000000):
            self.curr_index = (self.curr_index + self.steps) % i
            if self.curr_index == 0:
                n = i
            self.curr_index += 1
        return n

if __name__ == '__main__':
    spin = SpinLock(304)
    spin.loop()
    res = spin.state[1]
    print(res)
    spin2 = SpinLock(304)
    res = spin2.loop2()
    print(res)