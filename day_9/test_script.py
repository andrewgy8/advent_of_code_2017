from day_9.script import GarbageCleaner, get_file_and_format

inputs = [[1, "{}", 0],
          [6, "{{{}}}}", 0],
          [5, "{{},{}}", 0],
          [16, "{{{},{},{{}}}}", 0],
          [1, "{<a>,<a>,<a>,<a>}", 4],
          [9,  "{{<ab>},{<ab>},{<ab>},{<ab>!}}}}", 8],
          [9, "{{<!!>},{<!!>},{<!!>},{<!!>}}", 0],
          [3, "{{<a!>},{<a!>},{<a!>},{<ab>}}", 17],
          [43, "{{{{{{{{<!!!>!>!!oiau!>}}<u!!!!,!!,e!!!>'>}},{7}}}}}}}", 12]]


def test_counter_and_garbage():
    for i in inputs:
        score = i[0]
        c = GarbageCleaner(i[1])
        c.main()
        assert c.count == score
        assert c.garbage_count == i[2]


def test_final_parser():
    f = get_file_and_format()
    c = GarbageCleaner(f)
    c.main()
    assert c.count == 11898
    assert c.garbage_count == 5601

