

def main(source):
    sourceFile = open(source, 'r')
    lines = sourceFile.readlines()

    result1 = checkPasword(lines)
    print(result1)

    result2 = checkPasword2(lines)
    print(result2)


def checkPasword(lines):
    c = 0
    for line in lines:
        lowHigh, x, p = parseLine(line)

        count = p.count(x)
        if count >= lowHigh[0] and count <= lowHigh[1]:
            c += 1
    return c


def checkPasword2(lines):
    c = 0
    for line in lines:
        lowHigh, x, p = parseLine(line)

        letters = [p[i-1] for i in lowHigh]
        if letters.count(x) == 1:
            c += 1

    return c


def parseLine(line):
    s = line.split(' ')
    lowHigh = [int(x) for x in s[0].split('-')]
    x = s[1][0]
    p = s[2].rstrip('\n')

    return lowHigh, x, p


if __name__ == '__main__':
    challenge = '2-1'
    source = fr'..\resources\day{challenge}.txt'
    main(source)
