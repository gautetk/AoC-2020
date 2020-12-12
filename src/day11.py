
def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [x.rstrip('\n') for x in lines]
    t = {'L': 0, '.': '.'}
    inp = [[t['.']] * (len(inp[0])+2)] + [[t['.']] + [t[i] for i in x] + [t['.']] for x in inp] + [[t['.']] * (len(inp[0])+2)]

    result1 = part1(inp)
    print(result1)

    # result2 = part2(inp)
    # print(result2)

# def checkSeat


def part1(inp):
    
    print(inp)
    # inp.sort()
    # diff = [j-i for i, j in zip(inp, inp[1:])]
    # return diff.count(1) * diff.count(3)


def part2(inp):
    inp.sort()
    diff = [j-i for i, j in zip(inp[:-1], inp[1:])]

    # partition list into sublist, split on 3
    size = len(diff)
    idx_list = [idx + 1 for idx, val in enumerate(diff) if val == 3]
    zipIndex = zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))
    res = [len(diff[i: j-1]) for i, j in zipIndex]

    acc = 1
    asfd = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    for r in res:
        acc = acc * asfd[r]
    return acc


if __name__ == '__main__':
    challenge = '11'
    source = fr'resources\day{challenge}.txt'
    main(source)
