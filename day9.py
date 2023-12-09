def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read().strip()


def parse_input(a):
    b = a.split('\n')
    c = [[int(e) for e in d.split()] for d in b]
    return c


def recursive_thing(a):
    new = []
    for i in range(1, len(a)):
        new.append(a[i] - a[i-1])

    if set(new) == {0}:
        return a[0]

    return a[-1] + recursive_thing(new)


def recursive_thing_2(a):
    new = []
    for i in range(1, len(a)):
        new.append(a[i] - a[i-1])

    if set(new) == {0}:
        return a[0]

    return a[0] - recursive_thing_2(new)


def part_1():
    a = read_input('day9')
    b = parse_input(a)

    s = 0
    for c in b:
        s += recursive_thing(c)

    print(s)


def part_2():
    a = read_input('day9')
    b = parse_input(a)

    s = 0
    for c in b:
        s += recursive_thing_2(c)

    print(s)


part_1()
part_2()
