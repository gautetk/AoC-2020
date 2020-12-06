
def main(source):
    with open(source) as r:
        s = r.read()

    customStrings = parseInput(s)

    result1 = part1(customStrings)
    print(result1)

    result2 = part2(customStrings)
    print(result2)


def parseInput(s):
    return s.split('\n\n')


def part1(customStrings):
    groups = [g.replace('\n', '') for g in customStrings]
    return sum([len(set(g)) for g in groups])


def countUnique(group):
    answers = [set(x) for x in group.split('\n')]
    return len(set.intersection(*answers))


def part2(customStrings):
    return sum([countUnique(g) for g in customStrings])


if __name__ == '__main__':
    challenge = '6-1'
    source = fr'resources\day{challenge}.txt'
    main(source)
