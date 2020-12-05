import re


def main(source):
    with open(source) as r:
        lines = r.readlines()

    lines = [x.rstrip('\n') for x in lines]
    boardingPasses = parseInput(lines)

    result1 = part1(boardingPasses)
    print(result1)

    result2 = part2(boardingPasses)
    print(result2)



def getBoardingPass(b):
    row = int(b[:7].replace('F', '0').replace('B','1'),2)
    col = int(b[7:].replace('L', '0').replace('R','1'),2)
    bId = row * 8 + col
    return row, col, bId

def parseInput(lines):
    return [getBoardingPass(b) for b in lines]


def part1(boardingPasses):
    return max([bId for _, _, bId in boardingPasses])


def findSeat(bIds):
    for i, bId in enumerate(bIds):
        if bIds[i+1] == bId+2:
            return bId +1
    

def part2(boardingPasses):
    bIds = [bId for _, _, bId in boardingPasses]
    bIds.sort()
    return findSeat(bIds)


if __name__ == '__main__':
    challenge = '5-1'
    source = fr'resources\day{challenge}.txt'
    main(source)
