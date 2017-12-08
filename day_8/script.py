def get_file_and_format():
    with open('day_8/input.txt') as f:
        return [s.strip() for s in f.read().splitlines()]

values = {}

def main():
    max_value = 0

    cmds = get_file_and_format()
    cmds = [c.split(' ') for c in cmds]
    for cmd in cmds:
        diff = parse(cmd)
        if diff > max_value:
            max_value = diff

    print(values)
    res = values[get_max_val()]
    print(res, max_value)
    return res


def parse(cmd):
    val = cmd[0]
    dir = cmd[1]
    dir_val = int(cmd[2])

    condtional_val = cmd[4]
    operate = cmd[5]
    op_val = cmd[6]
    cond_curr_val = values.get(condtional_val, 0)
    if apply_operator(operate, cond_curr_val, op_val):
        this_value = values.get(val, 0)
        diff = inc_or_dec(this_value, dir, dir_val)


        values[val] = diff
        return diff
    return 0

def get_max_val():
    return max(values, key=lambda key: values[key])


def inc_or_dec(val, dir, dir_val):
    if dir == 'inc':
        return val + dir_val
    elif dir == 'dec':
        return val - dir_val
    else:
        print('this dir val does not exist')


def apply_operator(operate, val, compare_to):
    compare_to = int(compare_to)
    if operate == '>':
        return val > compare_to
    elif operate == '<':
        return val < compare_to
    elif operate == '==':
        return val == compare_to
    elif operate == '>=':
        return val >= compare_to
    elif operate == '<=':
        return val <= compare_to
    elif operate == '!=':
        return val != compare_to
    else:
        print('this oerator does not exist')

main()