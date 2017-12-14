from day_13.script import Scanner, parse

inputs = """0: 3
1: 2
4: 4
6: 4"""


def test_main():
    lines = parse(inputs)
    print(lines)
    scanner = Scanner(l=lines)
    res = scanner.main()
    assert res == 24