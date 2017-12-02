from itertools import permutations


def prep_table_from_string(inputs):
    """
    Takes string input and splits it into nested lists:
    Ex.
    3 4 32 5
    6 4 2 1
    48 5 9 
    
    :param inputs: 
    :return: [[3, 4, 32, 5], [6, 4, 2, 1], [48, 5, 9]]
    """
    table = [s.strip() for s in inputs.splitlines()]
    return [split_and_int(s) for s in table]


def split_and_int(s):
    return [int(s) for s in s.split()]


def get_diff_of_rows(i):
    sums = 0
    for row in prep_table_from_string(i):
        sums += min_and_max_in_row(row)
    return sums


def min_and_max_in_row(row):
    return max(row) - min(row)


def even_divisor_val(row):
    for x, y in permutations(row, 2):
        if x % y == 0:
            return x/y


def get_even_divisor_diff(i):
    sums = 0
    for row in prep_table_from_string(i):
        sums += even_divisor_val(row)
    return sums
