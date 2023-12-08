import re


def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read().strip()


def parse_input(a):
    b = a.split('\n')
    instructions = b[0]

    c = [re.findall('\w\w\w', d) for d in b[2:]]
    maps = {}
    for d in c:
        maps[d[0]] = {'L': d[1], 'R': d[2]}

    return instructions, maps


def part_1():
    a = read_input('day8')
    instructions, maps = parse_input(a)

    current = 'AAA'
    count = 0
    while current != 'ZZZ':
        i = instructions[count % len(instructions)]
        count += 1
        current = maps[current][i]

    print(count)


# Too slow
def part_2():
    a = read_input('day8')
    instructions, maps = parse_input(a)

    current = [b for b in maps.keys() if b[-1] == 'A']

    found = False
    count = 0
    while not found:
        found = True
        i = instructions[count % len(instructions)]
        count += 1
        new_current = []
        for pos in current:
            new_current.append(maps[pos][i])
            if maps[pos][i][-1] != 'Z':
                found = False

        current = new_current

    print(count)


def p2v2():
    a = read_input('day8')
    instructions, maps = parse_input(a)

    starts = [b for b in maps.keys() if b[-1] == 'A']
    vals = []

    for current in starts:
        count = 0
        pos = 0
        found = {}
        end = -1
        while (current, pos) not in found.keys():
            i = instructions[pos]

            found[(current, pos)] = count

            if current[-1] == 'Z' and end == -1:
                end = count

            count += 1
            pos = count % len(instructions)
            current = maps[current][i]

        vals.append({'z': end, 'loop': count - found[(current, pos)]})

    # Solve for count in the system of equations `count = z + k * loop` for any k.
    # In the case of the input, z==loop for each start, so
    # count = least_common_multiple(z)
    print(vals)


part_1()
# part_2()
p2v2()
