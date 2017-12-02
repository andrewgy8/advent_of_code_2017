from day_1.script import find_halfway_sum, find_looped_sum


def run_looped_sum_tests(i, sum):
    res = find_looped_sum(i)

    assert res == sum


def run_halfway_sum_tests(i, sum):
    res = find_halfway_sum(i)

    assert res == sum


def test_input_adds_sum():
    inputs = [[1122, 3], [1111, 4], [1234, 0], [91212129, 9]]

    for i in inputs:
        run_looped_sum_tests(i[0], i[1])


def test_halfway_sums():
    inputs = [[1212, 6], [1221, 0], [123425, 4], [123123, 12], [12131415, 4]]

    for i in inputs:
        run_halfway_sum_tests(i[0], i[1])
