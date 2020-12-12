import pprint


from math import degrees


def main(source):
    with open(source) as r:
        lines = r.readlines()

    inp = [x.rstrip('\n') for x in lines]
    t = {'L': 0, '.': None}
    seats = [[t['.']] * (len(inp[0])+2)] + [[t['.']] + [t[i] for i in x] + [t['.']] for x in inp] + [[t['.']] * (len(inp[0])+2)]

    result1 = part1(seats)
    print(result1)

    result2 = part2(seats)
    print(result2)


def checkSeat(square, seat):
    if seat == 0 and sum(filter(None, square)) == 0:
        return 1, 1

    if seat == 1 and sum(filter(None, square)) >= 4:
        return 1, 0
    return 0, seat


def interation(seats):
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
                        square = seats[y-1][x-1:x+2] + [seats[y][x-1], seats[y][x+1]] + seats[y+1][x-1:x+2]
                        dChanges, seat = checkSeat(square, seats[y][x])
                        changes += dChanges
                        row.append(seat)

            newSeats.append(row)
    return changes, newSeats


def part1(seats):
    changes = 1
    while changes > 0:
        changes, seats = interation(seats)
    return sum([sum(filter(None, row)) for row in seats])


def seeFn(x, y, seats):
    c = 0
    xTmp = x
    yTmp = y
    while xTmp > 0 and yTmp > 0:
        xTmp += -1
        yTmp += -1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while xTmp > 0 and yTmp < len(seats)-1:
        xTmp += -1
        yTmp += 1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while xTmp < len(seats[0])-1 and yTmp > 0:
        xTmp += 1
        yTmp += -1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while xTmp < len(seats[0])-1 and yTmp < len(seats)-1:
        xTmp += 1
        yTmp += 1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while xTmp < len(seats[0])-1:
        xTmp += 1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while xTmp > 0:
        xTmp += -1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while yTmp < len(seats)-1:
        yTmp += 1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    xTmp = x
    yTmp = y
    while yTmp > 0:
        yTmp += -1
        if seats[yTmp][xTmp] == 1:
            c += 1
            break
        if seats[yTmp][xTmp] == 0:
            break

    return c


def checkSeat2(see, seat):
    if seat == 0 and see == 0:
        return 1, 1
    if seat == 1 and see >= 5:
        return 1, 0
    return 0, seat


def interation2(seats):
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
                        see = seeFn(x, y, seats)
                        dChanges, seat = checkSeat2(see, seats[y][x])
                        changes += dChanges
                        row.append(seat)

            newSeats.append(row)
    return changes, newSeats


def part2(seats):
    changes = 1
    while changes > 0:
        changes, seats = interation2(seats)

    return sum([sum(filter(None, row)) for row in seats])


if __name__ == '__main__':
    challenge = '11'
    source = fr'resources\day{challenge}.txt'
    main(source)
