from itertools import chain, repeat


def get_file_and_format():
    with open('day_16/input.txt') as f:
        return f.read()


class DanceMoves:

    def __init__(self, moves, state):
        self.i = moves
        self.state = state
        self.seen = []

    def move(self):
        for move in self.i:
            type = move[0]
            if type == 's':
                self.spin(move)
            elif type == 'x':
                self.exchange(move)
            elif type == 'p':
                self.partner(move)
            else:
                print('doesnt exist')

    def dance(self, repeat=1):
        for i in range(0, repeat):
            state = ''.join(self.state)
            if state in self.seen:
                print(self.seen[repeat % i])
                return
            self.seen.append(state)
            self.move()

    def _ncycles(self, iterable, n):
        "Returns the sequence elements n times"
        return chain.from_iterable(repeat(tuple(iterable), n))

    def spin(self, move):
        length = len(self.state)
        spin_num = length - int(move[1:])
        l = spin_num + length
        arr = list(self._ncycles(self.state, 2))
        self.state = arr[spin_num:l]
        return self.state

    def exchange(self, move):
        move = move[1:]
        move = move.split('/')
        ex1 = int(move[0])
        ex2 = int(move[1])

        self.state[ex1], self.state[ex2] = self.state[ex2], self.state[ex1]

    def partner(self, move):
        move = move[1:]
        move = move.split('/')
        ex1 = move[0]
        ex2 = move[1]
        a, b = self.state.index(ex1), self.state.index(ex2)
        self.state[b], self.state[a] = self.state[a], self.state[b]

if __name__ == '__main__':
    i = get_file_and_format()
    i = i.split(',')
    initial_state = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    d = DanceMoves(i, initial_state)
    d.dance(1000000000)
    print(''.join(d.state))