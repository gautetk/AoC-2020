
def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [int(x.rstrip('\n')) for x in lines]
    inp += [0, max(inp)+3]

    result1 = part1(inp)
    print(result1)

    result2 = part2(inp)
    print(result2)


def part1(inp):
    inp.sort()
    diff = [j-i for i, j in zip(inp, inp[1:])]
    return diff.count(1) * diff.count(3)


def part2(inp):
    inp.sort()
    diff = [j-i for i, j in zip(inp[:-1], inp[1:])]

    size = len(diff)
    idx_list = [idx + 1 for idx, val in enumerate(diff) if val == 3]
    res = [len(diff[i: j-1]) for i, j in zip([0] + idx_list, idx_list + ([size] if idx_list[-1] != size else []))]

    acc = 1
    asfd = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    for r in res:
        acc = acc * asfd[r]
    return acc


if __name__ == '__main__':
    challenge = '10'
    source = fr'resources\day{challenge}.txt'
    main(source)
