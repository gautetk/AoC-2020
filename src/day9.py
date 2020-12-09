
def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [int(x.rstrip('\n')) for x in lines]
    lPre = 25

    result1 = part1(inp, lPre)
    print(result1)

    result2 = part2(inp, result1)
    print(result2)


def possibleSums(pre):
    valid = set()
    for i, v in enumerate(pre):
        for k in pre[i:]:
            valid.add(v+k)
    return valid


def part1(inp, lPre):
    pre = inp[:lPre]
    for i, v in enumerate(inp[lPre:]):
        pre = inp[i:lPre+i]
        if v not in possibleSums(pre):
            return v


def checkNumber(lines, result1):
    conNr = lines[0:1]
    for v in lines[1:]:
        conNr.append(v)
        if sum(conNr) == result1:
            return conNr


def part2(inp, result1):
    for i in range(len(inp)):
        conNr = checkNumber(inp[i:], result1)
        if conNr:
            return min(conNr) + max(conNr)


if __name__ == '__main__':
    challenge = '9-1'
    source = fr'resources\day{challenge}.txt'
    main(source)
