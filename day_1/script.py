from itertools import tee, chain, repeat


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def pairwise_halfway(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def prep_number(num):
    return [int(i) for i in str(num)]


def find_looped_sum(inputs):
    inputs = prep_number(inputs)
    p = list(pairwise(inputs))
    l = sum([0 + check_val(x) for x in p])
    if inputs[0] == inputs[-1]:
        l = l + inputs[-1]
    return l


def check_val(x):
    y, z = x
    if y == z:
        return y
    else:
        return 0


def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))


def find_halfway_sum(i):
    inputs = prep_number(i)
    length = len(inputs)
    l = list(ncycles(inputs, 2))
    sums = 0
    for i, x in enumerate(inputs):
        new_index = i + (length//2)
        if l[new_index] == x:
            sums += x
    return sums