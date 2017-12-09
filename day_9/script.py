def get_file_and_format():
    with open('day_9/input.txt') as f:
        return f.read()


class Counter:
    count = 0
    group_lvl = 0
    garbage_count = 0
    in_garbage = False
    escaped = False

    def __init__(self, input_str):
        self.input_str = list(input_str)

    def main(self):
        for i, v in enumerate(self.input_str):

            self.escaped = self.determine_escapism(v, i)

            if self.in_garbage:
                self.in_garbage = self.garbage_processor(v)
            else:
                self.group_counter(v)

    def determine_escapism(self, v, i):
        if self.input_str[i - 1] == '!':
            if v == '!':
                self.input_str[i] = 'N'
            return True
        return False

    def garbage_processor(self, v):
        if self.escaped:
            return self.in_garbage

        if v == '>':
            return False
        elif v != '!':
            self.garbage_count += 1
            return True
        return self.in_garbage

    def group_counter(self, v):
        if self.escaped:
            return

        if v == '{':
            self.group_lvl += 1
        elif v == '}':
            self.count += self.group_lvl
            self.group_lvl -= 1
        elif v == '<':
            self.in_garbage = True


f = get_file_and_format()
c = Counter(f)
c.main()
print("Full group count: ", c.count)
print("Garbage character count: ", c.garbage_count)