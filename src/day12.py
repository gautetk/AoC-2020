import math


def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [x.rstrip('\n') for x in lines]
    inp = [(x[0], int(x[1:])) for x in inp]

    result1 = part1(inp)
    print(result1)

    result2 = part2(inp)
    print(result2)


instructions = {
    'N': (0, 1, 0),
    'S': (0, -1, 0),
    'E': (1, 0, 0),
    'W': (-1, 0, 0),
    'R': (0, 0, -1),
    'L': (0, 0, 1),
}


def moveRotate(instruct, v):
    return [i * v for i in instruct]


def forward(head, v):
    h = head % 360
    if h == 0:
        instruct = instructions['E']
    elif h == 90:
        instruct = instructions['N']
    elif h == 180:
        instruct = instructions['W']
    elif h == 270:
        instruct = instructions['S']
    return moveRotate(instruct, v)


def part1(inp):
    x = 0
    y = 0
    head = 0
    for c in inp:
        if c[0] == 'F':
            dx, dy, dHead = forward(head, c[1])
        else:
            dx, dy, dHead = moveRotate(instructions[c[0]], c[1])
        x += dx
        y += dy
        head += dHead
    return abs(x)+abs(y)


def moveWP(instruct, v):
    return instruct[0]*v, instruct[1]*v


def rotateWP(xW, yW, rot):
    r = math.radians(rot % 360)
    dx = int(round(xW*math.cos(r)-yW*math.sin(r)))
    dy = int(round(xW*math.sin(r)+yW*math.cos(r)))
    return dx, dy


def part2(inp):
    x = 0
    y = 0
    xW = 10
    yW = 1
    for c in inp:
        if c[0] == 'F':
            x += xW * c[1]
            y += yW * c[1]
        else:
            if c[0] == 'L':
                xW, yW = rotateWP(xW, yW, c[1])
            elif c[0] == 'R':
                xW, yW = rotateWP(xW, yW, -c[1])
            else:
                dx, dy = moveWP(instructions[c[0]], c[1])
                xW += dx
                yW += dy

    return abs(x)+abs(y)


if __name__ == '__main__':
    challenge = '12'
    source = fr'resources\day{challenge}.txt'
    main(source)
