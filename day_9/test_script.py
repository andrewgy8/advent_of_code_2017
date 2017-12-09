from day_9.script import Counter

inputs = [[1, "{}", 0],
          [6, "{{{}}}}}", 0],
          [5, "{{},{}}", 0],
          [16, "{{{},{},{{}}}}", 0],
          [1, "{<a>,<a>,<a>,<a>}", 4],
          [9,  "{{<ab>},{<ab>},{<ab>},{<ab>!}}}}", 8],
          [9, "{{<!!>},{<!!>},{<!!>},{<!!>}}", 0],
          [3, "{{<a!>},{<a!>},{<a!>},{<ab>}}", 17],
          [43, "{{{{{{{{<!!!>!>!!oiau!>}}<u!!!!,!!,e!!!>'>}},{7}}}}}}}", 12]]


def test_counter():
    for i in inputs:
        score = i[0]
        c = Counter(i[1])
        res = c.parse()
        assert res == score


def test_remove_garbage():
    for i in inputs:
        score = i[0]
        c = Counter(i[1])
        c.parse()
        assert c.count == score
        assert c.garbage_count == i[2]