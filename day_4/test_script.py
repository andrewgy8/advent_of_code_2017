from day_4.script import check_dupes


def test_main():
    str_1 = "a b c d e f"
    res = check_dupes(str_1)
    assert not res

    str_2 = "a b c a d"
    res = check_dupes(str_2)
    assert res
