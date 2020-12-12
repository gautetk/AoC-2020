import math


def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [x.rstrip('\n') for x in lines]
    inp = [(x[0], int(x[1:])) for x in inp]

    instructions = {
        'N': (0, 1, 0),
        'S': (0, -1, 0),
        'E': (1, 0, 0),
        'W': (-1, 0, 0),
        'R': (0, 0, -1),
        'L': (0, 0, 1),
        0: (1, 0, 0),
        90: (0, 1, 0),
        180: (-1, 0, 0),
        270: (0, -1, 0),
    }

    result1 = part1(inp, instructions)
    print(result1)

    result2 = part2(inp, instructions)
    print(result2)


def part1(inp, instructions):
    x = 0
    y = 0
    head = 0
    for c in inp:
        if c[0] == 'F':
            instruct = instructions[head % 360]
        else:
            instruct = instructions[c[0]]

        dx, dy, dHead = moveRotate(instruct, c[1])
        x += dx
        y += dy
        head += dHead
    return abs(x)+abs(y)


def part2(inp, instructions):
    x = 0
    y = 0
    xW = 10
    yW = 1
    for c in inp:
        if c[0] == 'F':
            x += xW * c[1]
            y += yW * c[1]
        else:
            instruct = instructions[c[0]]
            xW, yW = rotateWP(xW, yW, instruct[-1], c[1])
            dx, dy = moveRotate(instruct[:-1], c[1])
            xW += dx
            yW += dy

    return abs(x)+abs(y)


def moveRotate(instruct, v):
    return [i * v for i in instruct]


def rotateWP(xW, yW, dir, rot):
    r = math.radians(dir*rot % 360)
    dx = int(round(xW*math.cos(r)-yW*math.sin(r)))
    dy = int(round(xW*math.sin(r)+yW*math.cos(r)))
    return dx, dy


if __name__ == '__main__':
    challenge = '12'
    source = fr'resources\day{challenge}.txt'
    main(source)
