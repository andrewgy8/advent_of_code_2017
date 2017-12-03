from day_3.script import main, main_2


def test_access_port_steps():
    res = main(23)
    assert res == 2
    res = main(1024)
    assert res == 31


def test_part_b():
    res = main_2(1)
    assert res == 1
    res = main_2(5)
    assert res == 5
    res = main_2(6)
    assert res == 10
    res = main_2(8)
    assert res == 23