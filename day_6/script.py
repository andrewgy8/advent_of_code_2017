
class Redistribution:
    prev_dist = []
    previously_existent = False
    cycles = 0

    def __init__(self, dist):
        self.dist = dist

    def main(self):
        while not self.previously_existent:
            self.cycles += 1
            prev = self.dist[:]
            self.prev_dist.append(prev)
            self.distribute()

            if self.check_prev():
                return self.cycles

    def distribute(self):
        val = max(self.dist)
        max_index = [x for x in range(len(self.dist)) if self.dist[x] == val][0]
        self.cycle_from(self.add_one, max_index)
        return self.dist

    def add_one(self, i):
        return i + 1

    def check_prev(self):
        if self.dist in self.prev_dist:
            turn = self.prev_dist.index(self.dist)
            print(self.cycles - turn)
            self.previously_existent = False
            return True
        return False

    def cycle_from(self, func, start_index):
        nxt_index = start_index
        times = self.dist[start_index]
        self.dist[start_index] = 0

        for _ in range(0, times):
            nxt_index += 1
            if nxt_index >= len(self.dist):
                nxt_index = 0
            tgt = self.dist[nxt_index]
            self.dist[nxt_index] = func(tgt)

        return self.dist

i = [2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]
r = Redistribution(i)
res = r.main()
print(res)