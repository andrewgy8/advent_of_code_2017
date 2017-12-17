from day_17.script import SpinLock

def test_spin():
    spin = SpinLock(3)
    spin.loop()
    assert spin.state[spin.curr_index+1] == 638