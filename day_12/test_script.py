from day_12.script import TravelingSalesman, get_file_and_format

inputs = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""


def test_script():
    t = TravelingSalesman(inputs)
    t.parse()
    res = t.cycle_through_relationships()
    assert res == 6

    i = get_file_and_format()
    t = TravelingSalesman(i)
    t.parse()

    # res = t.cycle_through_relationships()
    # assert res == 152