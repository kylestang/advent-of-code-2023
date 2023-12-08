import re


def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read().strip()


def part_1():
    inputs = read_input('day6').split('\n')

    times = [int(b) for b in re.split(' +', inputs[0])[1:]]
    dists = [int(b) for b in re.split(' +', inputs[1])[1:]]

    possibilities = 1

    for i in range(len(times)):
        p = 0
        for hold_t in range(1, times[i]):
            if hold_t * (times[i] - hold_t) > dists[i]:
                p += 1

        possibilities *= p

    print(possibilities)


def part_2():
    inputs = read_input('day6').split('\n')

    times = [b for b in re.split(' +', inputs[0])[1:]]
    dists = [b for b in re.split(' +', inputs[1])[1:]]

    t = int(''.join(times))
    d = int(''.join(dists))

    possibilities = 0

    for hold_t in range(1, t):
        if hold_t * (t - hold_t) > d:
            possibilities += 1

    print(possibilities)


part_1()
part_2()
