from day_11.script import main


def test_main():
    i = ['ne', 'ne', 'ne']
    res = main(i)
    assert res[0] == 3
    i = ['ne','ne','sw','sw']
    res = main(i)
    assert res[0] == 0
    i = ['ne','ne','s','s']
    res = main(i)
    assert res[0] == 2
    i = ['se','sw','se','sw','sw']
    res = main(i)
    assert res[0] == 3

