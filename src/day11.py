
def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [x.rstrip('\n') for x in lines]
    t = {'L': 0, '.': None}
    # add floor around all seats
    seats = [[t['.']] * (len(inp[0])+2)] + [[t['.']] + [t[i] for i in x] + [t['.']] for x in inp] + [[t['.']] * (len(inp[0])+2)]

    result1 = part1(seats)
    print(result1)

    result2 = part2(seats)
    print(result2)


def part1(seats):
    changes = 1
    while changes > 0:
        changes, seats = interation(seats, adjacent, 4)

    return sum([sum(filter(None, row)) for row in seats])


def part2(seats):
    changes = 1
    while changes > 0:
        changes, seats = interation(seats, see, 5)

    return sum([sum(filter(None, row)) for row in seats])


def interation(seats, rule, maxNr):
    changes = 0
    newSeats = []
    for y in range(len(seats)):
        if y == 0 or y == len(seats)-1:
            newSeats.append([None]*len(seats[0]))
        else:
            row = []
            for x in range(len(seats[0])):
                if x == 0 or x == len(seats[0])-1:
                    row.append(None)
                else:
                    if seats[y][x] == None:
                        row.append(None)
                    else:
                        nrPeople = rule(x, y, seats)
                        dChanges, seat = checkSeat(nrPeople, seats[y][x], maxNr)
                        changes += dChanges
                        row.append(seat)

            newSeats.append(row)
    return changes, newSeats


def checkSeat(nrPeople, seat, maxNr):
    if seat == 0 and nrPeople == 0:
        return 1, 1
    if seat == 1 and nrPeople >= maxNr:
        return 1, 0
    return 0, seat


def adjacent(x, y, seats):
    square = seats[y-1][x-1:x+2] + [seats[y][x-1], seats[y][x+1]] + seats[y+1][x-1:x+2]
    return sum(filter(None, square))


def checkDir(x, y, dx, dy, seats):
    xTmp = x
    yTmp = y
    while 0 < xTmp < len(seats[0])-1 and 0 < yTmp < len(seats)-1:
        xTmp += dx
        yTmp += dy
        if seats[yTmp][xTmp] != None:
            return seats[yTmp][xTmp]
    return 0


def see(x, y, seats):
    directions = [
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    return sum([checkDir(x, y, dx, dy, seats) for dx, dy in directions])


if __name__ == '__main__':
    challenge = '11'
    source = fr'resources\day{challenge}.txt'
    main(source)
