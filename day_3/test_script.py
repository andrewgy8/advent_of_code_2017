from day_3.script import main, main_2


def test_access_port_steps():
    res = main(23)
    assert res == 2
    res = main(1024)
    assert res == 31


def test_solution():
    res = main_2(277678)
    assert res == 279138


def test_part_b():
    res = main_2(1)
    assert res == 2
    res = main_2(5)
    assert res == 10
    res = main_2(10)
    assert res == 11
    res = main_2(11)
    assert res == 23
    res = main_2(25)
    assert res == 26
    res = main_2(747)
    assert res == 806