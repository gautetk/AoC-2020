from more_itertools import locate



def main(source):
    with open(source) as r:
        line = r.readline()

    numbers = [int(x) for x in line.rstrip('\n').split(',')]

    result1 = part1(numbers)
    print(result1)

    # result2 = part2(data)
    # print(result2)


def parseLine(line):
    if line[0] == 'mask':
        return line
    else:
        return int(line[0].split('[')[-1][:-1]), int(line[1])

def writeMemory(mask, value):
    def check(m,v): 
        if m == 'X':
            return v
        else: 
            return m
    return int(''.join([check(m,v) for m, v in zip(mask, value)]),2)



def part1(numbers):
    for i in range(len(numbers),30000000):
        last = numbers[-1]
        indexes = list(locate(numbers, lambda a: a==last))
        # print(indexes)
        if len(indexes) == 1:
            numbers.append(0)
        else:
            numbers.append(indexes[-1]-indexes[-2])
            # print(numbers)
            # b=b



    # mem = {}
    # for i, d in enumerate(data):
    #     if d[0]=='mask':
    #         mask = d[1]
    #     else:
    #         mem[d[0]] = writeMemory(mask, intToBi(d[1]))
    return numbers[-10:]


def part2(data):
    mem = {}
    for d in data:
        if d[0]=='mask':
            mask = d[1]
        else:
            memLocs = memoryLoc(mask,intToBi(d[0]))
            for loc in memLocs:
                mem[loc] = d[1]
    return sum(mem.values())
        
def memoryLoc(mask, value):
    floatBits = []
    maskedValues = []
    for i, mv in enumerate(zip(mask, value)):
        m, v = mv
        if m == '0':
            maskedValues.append(v)
        elif m == '1':
            maskedValues.append(m)
        else: 
            maskedValues.append(i)
            floatBits.append(i)
    locations = []
    for combo in list(product(range(2), repeat=len(floatBits))):
        tmpList = maskedValues.copy()
        for i, v in zip(floatBits, combo):
            tmpList[i] = str(v)
        loc = int(''.join(tmpList),2)
        locations.append(loc)

    return locations





def intToBi(i):
    bi = f'{i:b}'
    return '0'*(36-len(bi))+bi

if __name__ == '__main__':
    challenge = '15'
    source = fr'resources\day{challenge}.txt'
    main(source)
