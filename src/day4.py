import re


def main(source):
    with open(source) as r:
        s = r.read()

    infos = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    result1 = part1(s, infos)
    print(result1)

    result2 = part2(s, infos)
    print(result2)


def parseInput(s):
    passportStrings = s.split('\n\n')
    return [mDict(re.split('\n| ', p)) for p in passportStrings]


def mDict(p):
    return {i.split(':')[0]: i.split(':')[1] for i in p}


def minMaxInt(vMin, vMax, v):
    if not v.isdigit():
        return False
    return vMin <= int(v) <= vMax


def validateHeight(hgt):
    if hgt.endswith('cm'):
        return minMaxInt(150, 193, hgt.strip('cm'))
    elif hgt.endswith('in'):
        return minMaxInt(59, 76, hgt.strip('in'))
    else:
        return False


def validateValues(p):
    valids = [
        minMaxInt(1920, 2002, p['byr']),
        minMaxInt(2010, 2020, p['iyr']),
        minMaxInt(2020, 2030, p['eyr']),
        validateHeight(p['hgt']),
        re.match("^#[a-z0-9]{6}$", p['hcl']) != None,
        p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        p['pid'].isdigit(),
        len(p['pid']) == 9,
    ]
    return all(valids)


def checkPassport1(infos, p):
    return all(k in p for k in infos)


def checkPassport2(infos, p):
    if all(k in p for k in infos):
        return validateValues(p)
    else:
        return False


def part1(s, infos):
    passports = parseInput(s)
    valid = [checkPassport1(infos, p) for p in passports]

    return sum(valid)


def part2(s, infos):
    passports = parseInput(s)
    valid = [checkPassport2(infos, p) for p in passports]

    return sum(valid)


if __name__ == '__main__':
    challenge = '4-1'
    source = fr'resources\day{challenge}.txt'
    main(source)
