from collections import deque
from functools import reduce
from operator import xor


def knot_hash_list(lengths, cycle_size=256, iterations=64):
    seq = deque(range(cycle_size))
    skip = 0

    for _ in range(iterations):
        for l in lengths:
            seq.extend(reversed(deque(seq.popleft() for _ in range(l))))
            seq.rotate(-skip)
            skip += 1

    seq.rotate(iterations * sum(lengths) + skip * (skip-1) // 2)
    seq = list(seq)
    return [reduce(xor, seq[i:i+16]) for i in range(0, cycle_size, 16)]


def str_to_lengths(s, extend=()):
    return [ord(x) for x in s] + list(extend)


def convert_to_bin(hex):
    print(hex)
    hex = ''.join([str(n) for n in hex])
    print(hex)
    return bin(int(hex, 16))[2:].zfill(128)


def count_ones(string):
    return string.count('1')


def get_row_inputs(inputs):
    count = 0
    for n in range(0, 128):
        i = inputs + "-{n}".format(n=n)
        l = str_to_lengths(i)
        k = knot_hash_list(l)
        b = convert_to_bin(k)
        res = count_ones(b)
        count += res
    return count


if __name__ == '__main__':
    inputs = 'uugsqrei'
    res = get_row_inputs(inputs)
    print(res)
