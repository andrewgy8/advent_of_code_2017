from itertools import permutations


def prep_table(inputs):
    table = [s.strip() for s in inputs.splitlines()]
    return [split_and_int(s) for s in table]


def split_and_int(s):
    string_lst = s.split()
    return [int(s) for s in string_lst]


def get_diff_of_rows(i):
    table = prep_table(i)
    sums = 0
    for row in table:
        sums += min_and_max_in_row(row)
    return sums


def min_and_max_in_row(row):
    low = min(row)
    high = max(row)
    return high - low


def even_divisor_val(row):
    combos = permutations(row, 2)
    for x, y in combos:
        if x % y == 0:
            return x/y


def get_even_divisor_diff(i):
    table = prep_table(i)
    sums = 0
    for row in table:
        sums += even_divisor_val(row)
    return sums