import re


def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read()


def part_1():
    c = read_input('day1')

    t = 0
    for b in c.split('\n')[:-1]:
        a = re.sub('\D', '', b)
        t += int(a[0] + a[-1])

    print(t)


def part_2():
    c = read_input('day1')

    t = 0
    for b in c.split('\n')[:-1]:
        a = re.sub('one', 'one1one', b)
        a = re.sub('two', 'two2two', a)
        a = re.sub('three', 'three3three', a)
        a = re.sub('four', 'four4four', a)
        a = re.sub('five', 'five5five', a)
        a = re.sub('six', 'six6six', a)
        a = re.sub('seven', 'seven7seven', a)
        a = re.sub('eight', 'eight8eight', a)
        a = re.sub('nine', 'nine9nine', a)
        a = re.sub('\D', '', a)
        t += int(a[0] + a[-1])

    print(t)


part_1()
part_2()
