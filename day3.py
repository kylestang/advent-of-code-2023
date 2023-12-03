import string

def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read()


def part_1():
    a = read_input('day3').split('\n')[:-1]
    a.insert(0, '.' * len(a[0]))
    a.append('.' * len(a[0]))

    a = ['..' + b + '..' for b in a]
    sum = 0

    for y in range(1, len(a) - 1):
        num = 0
        power = 1
        part = False
        for x in range(len(a[0]) - 2, 0, -1):
            if a[y][x] in string.punctuation:
                if part:
                    sum += num
                    part = False
                num = 0
                power = 1
            elif a[y][x] in string.digits:
                num += int(a[y][x]) * power
                power *= 10
                if adjacent(a, y, x):
                    part = True

    print(sum)


def adjacent(a, y, x):
    s = string.punctuation.replace('.','')

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if a[y + i][x + j] in s:
                return True

    return False


def a2(a, y, x):
    g = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if a[y + i][x + j] == '*':
                g.append(f'{y+i}:{x+j}')

    return g


def part_2():
    a = read_input('day3').split('\n')[:-1]
    a.insert(0, '.' * len(a[0]))
    a.append('.' * len(a[0]))

    a = ['..' + b + '..' for b in a]
    g = {}

    for y in range(1, len(a) - 1):
        num = 0
        power = 1
        b = []
        for x in range(len(a[0]) - 2, 0, -1):
            if a[y][x] in string.punctuation:
                for c in set(b):
                    if c in g:
                        g[c].append(num)
                    else:
                        g[c] = [num]
                b = []
                num = 0
                power = 1
            elif a[y][x] in string.digits:
                num += int(a[y][x]) * power
                power *= 10
                b += a2(a, y, x)

    sum = 0
    for d in g.values():
        if len(d) == 2:
            sum += d[0] * d[1]

    print(sum)


part_1()
part_2()
