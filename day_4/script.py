from collections import Counter


def get_file_and_format():
    with open('day_4/input.txt') as f:
        return [s.strip() for s in f.read().splitlines()]


def main():
    passes = get_file_and_format()
    count = 0
    for phrase in passes:
        dupe = check_dupes(phrase)
        ana = check_anagrams(phrase)
        if not dupe and not ana:
            count += 1

    return count


def check_dupes(pass_phrase):
    passes = pass_phrase.split(' ')
    val = [k for k, v in Counter(passes).items() if v > 1]
    return val


def check_anagrams(pass_phrase):
    words = pass_phrase.split(' ')
    matches = 0
    for word in words:
        l = list(word)
        for c in words:
            chk = list(c)
            if sorted(chk) == sorted(l) and not (word == c):
                matches += 1
    if matches < 2:
        return False
    else:
        return True

res = main()
