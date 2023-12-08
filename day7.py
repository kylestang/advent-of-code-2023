def read_input(name: str) -> str:
    with open('inputs/' + name, 'r') as f:
        return f.read().strip()

values = {'A':22, 'K':21, 'Q': 20, 'J': 19, 'T': 18, '9': 17, '8': 16, '7': 15, '6': 14, '5': 13, '4': 12, '3': 11, '2':10}
values2 = {'A':22, 'K':21, 'Q': 20, 'J': 10, 'T': 19, '9': 18, '8': 17, '7': 16, '6': 15, '5': 14, '4': 13, '3': 12, '2':11}

def parse_hand(a):
    b = [j.split() for j in a.split('\n')]
    c = [{'hand': [values[h] for h in list(k[0])], 'bid': int(k[1])} for k in b]
    return c


def parse_hand2(a):
    b = [j.split() for j in a.split('\n')]
    c = [{'hand': [values2[h] for h in list(k[0])], 'bid': int(k[1])} for k in b]
    return c


def score(hand):
    hand = hand['hand']
    val = int(''.join([str(i) for i in hand]))
    hand = list(sorted(hand))
    if len(set(hand)) == 1:
        return 6*10**15 + val
    elif hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
        return 5*10**15 + val
    elif len(set(hand)) == 2:
        return 4*10**15 + val
    elif hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
        return 3*10**15 + val
    elif len(set(hand)) == 3:
        return 2*10**15 + val
    elif len(set(hand)) == 4:
        return 1*10**15 + val
    else:
        return val


def recursive_thing(hand):
    jokers = list(range(11, 23))

    if 10 in hand:
        best = 0
        pos = hand.index(10)

        for j in jokers:
            new_hand = hand.copy()
            new_hand[pos] = j
            value = recursive_thing(new_hand)
            if value > best:
                best = value

        return best

    else:
        hand = list(sorted(hand))
        if len(set(hand)) == 1:
            return 6
        elif hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
            return 5
        elif len(set(hand)) == 2:
            return 4
        elif hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
            return 3
        elif len(set(hand)) == 3:
            return 2
        elif len(set(hand)) == 4:
            return 1
        else:
            return 0


def score2(hand):
    hand = hand['hand']
    val = int(''.join([str(i) for i in hand]))

    hand_class = recursive_thing(hand)
    return hand_class*10**15 + val


def part_1():
    a = read_input('day7')
    b = parse_hand(a)
    c = sorted(b, key=score)

    s = 0

    for i in range(len(c)):
        s += c[i]['bid'] * (i+1)

    print(s)


def part_2():
    a = read_input('day7')
    b = parse_hand2(a)
    c = sorted(b, key=score2)

    s = 0

    for i in range(len(c)):
        s += c[i]['bid'] * (i+1)

    print(s)


part_1()
part_2()
