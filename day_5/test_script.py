from day_5.script import Walker

i = ["0", "3", "0", "1", "-3"]


def test_main():
    w = Walker(i)
    res = w.main()
    assert res == 5


def test_main_two():
    w = Walker(i, True)
    res = w.main()
    assert res == 10