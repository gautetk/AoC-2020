


def main(source):
    sourceFile = open(source, 'r')
    sourceLines = sourceFile.readlines()
    lines = [int(s) for s in sourceLines]

    result1 = loop(lines)
    print(result1)

    result2 = tripleLoop(lines)
    print(result2)


def loop(lines):

    for i, x in enumerate(lines):
        for y in lines[i:]:
            if x+y==2020:
                return(x*y)

def tripleLoop(lines):

    for i, x in enumerate(lines):
        for j, y in enumerate(lines[i:], start=i):
            for z in lines[j:]:
                if x+y+z==2020:
                    return(x*y*z)
                    

if __name__ == '__main__':
    challenge = '1-1'
    source = fr'..\resources\day{challenge}.txt'
    main(source)

