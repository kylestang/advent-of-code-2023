import re


def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read()


def part_1():
    a = read_input('day4')
    a = a.split('\n')[:-1]
    b = [c.split(':')[1].split('|') for c in a]
    b = [{'wins': [int(e) for e in re.split(' +', f[0].strip())],
          'nums': [int(g) for g in re.split(' +', f[1].strip())]} for f in b]

    s = 0
    for c in b:
        t = 0
        for d in c['wins']:
            if d in c['nums']:
                if t == 0:
                    t = 1
                else:
                    t *= 2

        s += t

    print(s)


# Technically works, but takes 20 seconds to run (or 3 seconds with pypy)
def part_2():
    a = read_input('day4')
    a = a.split('\n')[:-1]
    b = [c.split(':')[1].split('|') for c in a]
    b = [{'card': i, 'wins': [int(e) for e in re.split(' +', f[0].strip())],
          'nums': [int(g) for g in re.split(' +', f[1].strip())]}
         for i, f in enumerate(b)]

    c = 0
    while c < len(b):
        t = 1
        for d in b[c]['wins']:
            if d in b[c]['nums']:
                b.append(b[b[c]['card'] + t])
                t += 1

        c += 1

    print(len(b))


# A bit better solution
def part_2v2():
    a = read_input('day4')
    a = a.split('\n')[:-1]
    b = [c.split(':')[1].split('|') for c in a]
    b = [{'card': i, 'wins': [int(e) for e in re.split(' +', f[0].strip())],
          'nums': [int(g) for g in re.split(' +', f[1].strip())]}
         for i, f in enumerate(b)]

    c = [0] * len(b)

    for e in reversed(b):
        t = 1
        s = 1
        for d in e['wins']:
            if d in e['nums']:
                s += c[e['card'] + t]
                t += 1

        c[e['card']] = s

    print(sum(c))


part_1()
part_2()
part_2v2()
