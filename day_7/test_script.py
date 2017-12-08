from day_7.script import Network


def test_nework():
    n = Network()
    res = n.build_tree()
    assert res == 'tknk'
