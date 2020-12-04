import re


def main(source):
    with open(source) as r:
        s = r.read()

    infos = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid',
    ]

    result1 = part1(s, infos)
    print(result1)

    result2 = part2(s, infos)
    print(result2)


def parseInput(s):
    passportStrings = s.split('\n\n')
    return [mDict(re.split('\n| ', p)) for p in passportStrings]


def mDict(p):
    return {i.split(':')[0]: i.split(':')[1] for i in p}


def minMaxInt(vmin, vmax, v):
    if not v.isdigit():
        return 0
    if int(v) < vmin or int(v) > vmax:
        return 0
    return 1


def validateValues(p):
    if minMaxInt(1920, 2002, p['byr']) == 0:
        return 0

    if minMaxInt(2010, 2020, p['iyr']) == 0:
        return 0

    if minMaxInt(2020, 2030, p['eyr']) == 0:
        return 0

    hgt = p['hgt']
    if hgt.strip('0123456789') == 'cm':
        if minMaxInt(150, 193, hgt.strip('cm')) == 0:
            return 0
    elif hgt.strip('0123456789') == 'in':
        if minMaxInt(59, 76, hgt.strip('in')) == 0:
            return 0
    else:
        return 0

    hcl = p['hcl']
    if not hcl[0] == '#':
        return 0
    if not len(hcl) == 7:
        return 0
    if not re.match("^[a-z0-9_-]*$", hcl[1:]):
        return 0

    ecl = p['ecl']
    if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 0

    pid = p['pid']
    if not pid.isdigit():
        return 0
    if not len(pid) == 9:
        return 0

    return 1


def checkPassport1(infos, p):
    if all(k in p for k in infos):
        return 1
    else:
        return 0


def checkPassport2(infos, p):
    if all(k in p for k in infos):
        return validateValues(p)
    else:
        return 0


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
