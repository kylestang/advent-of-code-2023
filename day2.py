def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read()


def part_1():
    a = read_input("day2")

    lines = a.split('\n')[:-1]
    games = [create_game(l) for l in lines]
    sum = 0

    for g in games:
        v = True

        for d in g['cubes']:
            if d['r'] > 12 or d['g'] > 13 or d['b'] > 14:
                v = False
                break

        if v:
            sum += g['id']

    print(sum)


def create_game(line: str):
    gid = int(line.split(' ')[1][:-1])
    info = line.split(':')[1]
    draws = info.split(';')
    cubes = create_cubes(draws)
    a = {'id': gid, 'cubes': cubes}
    return a


def create_cubes(draws: list[str]):
    a = []
    for draw in draws:
        r = 0
        g = 0
        b = 0
        colours = draw.split(',')
        for c in colours:
            num, colour = c.strip().split(' ')
            num = int(num)
            if colour == 'red':
                r = num
            elif colour == 'green':
                g = num
            elif colour == 'blue':
                b = num
            else:
                exit(1)

        a.append({'r': r, 'g': g, 'b': b})

    return a


def part_2():
    a = read_input("day2")

    lines = a.split('\n')[:-1]
    games = [create_game(l) for l in lines]

    p = 0
    for game in games:
        r = 0
        g = 0
        b = 0

        for c in game['cubes']:
            r = max(r, c['r'])
            g = max(g, c['g'])
            b = max(b, c['b'])

        p += r * g * b

    print(p)


part_1()
part_2()
