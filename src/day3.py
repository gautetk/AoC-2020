import math


def main(source):
    sourceFile = open(source, 'r')
    lines = sourceFile.readlines()
    s = [x.rstrip('\n') for x in lines]

    result1 = part1(s)
    print(result1)

    result2 = part2(s)
    print(result2)


def part1(s):
    dx = 3
    dy = 1
    return checkSlope(s, dx, dy)


def part2(s):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    return math.prod([checkSlope(s, dx, dy) for dx, dy in slopes])


def checkSlope(s, dx, dy):
    nx = len(s[0])
    c = 0
    x = 0
    y = 0
    while y+dy < len(s):
        x = x + dx
        y = y + dy
        if s[y][x % nx] == '#':
            c += 1
    return c


if __name__ == '__main__':
    challenge = '3-1'
    source = fr'..\resources\day{challenge}.txt'
    main(source)
