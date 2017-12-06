from day_6.script import Redistribution



def test_main():
    lst = [0, 2, 7, 0]

    r = Redistribution(lst)
    res = r.main()
    assert res == 5


def test_cycle():
    lst = [0, 2, 7, 0]

    r = Redistribution(lst)

    def add_o(i):
        return i + 1

    res = r.cycle_from(add_o, 2)

    assert res == [2, 4, 1, 2]

