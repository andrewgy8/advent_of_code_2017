from day_16.script import DanceMoves


def test_spin_move():
    inputs = list("abcde")
    d = DanceMoves(moves=[], state=inputs)
    d.spin('s1')
    assert ''.join(d.state) == 'eabcd'
    d.state = inputs
    d.spin('s3')
    assert ''.join(d.state) == 'cdeab'


def test_exchange_move():
    inputs = list("abcde")
    d = DanceMoves(moves=[], state=inputs)
    d.spin('s1')
    d.exchange('x3/4')
    assert ''.join(d.state) == 'eabdc'
    # d.state = inputs
    # d.exchange('x3')
    # assert ''.join(d.state) == 'cdeab'


def test_partner_move():
    inputs = list("abcde")
    d = DanceMoves(moves=[], state=inputs)
    d.spin('s1')
    d.exchange('x3/4')
    d.partner('pe/b')
    assert ''.join(d.state) == 'baedc'


