def get_file_and_format():
    with open('day_9/input.txt') as f:
        return f.read()


class Counter:
    count = 0
    last_count = 0
    garbage_count = 0
    in_garbage = False
    escaped = False

    def __init__(self, input_str):
        self.input_str = list(input_str)

    def parse(self):
        for i, v in enumerate(self.input_str):
            if v == '!':
                if self.input_str[i - 1] == '!':
                    self.escaped = True
                    self.input_str[i] = 'N'
                elif not self.escaped and self.input_str[i - 1] == '!':
                    self.escaped = True
            elif self.input_str[i - 1] == '!':
                self.escaped = True
            elif self.input_str[i - 1] != '!':
                self.escaped = False
            else:
                self.escaped = False

            if not self.in_garbage:
                if v == '{' and not self.escaped:
                    self.last_count += 1

                elif v == '}' and not self.escaped:
                    self.count += self.last_count
                    self.last_count -= 1
                    if self.last_count < 0:
                        self.last_count = 0
                elif v == '<' and not self.escaped:
                    self.in_garbage = True
            else:
                if v == '>' and not self.escaped:
                    self.in_garbage = False
                elif not self.escaped and v != '!':
                    self.garbage_count += 1
                    self.in_garbage = True

        return self.count

f = get_file_and_format()
c = Counter(f)
res = c.parse()
print(c.count)
print(c.garbage_count)