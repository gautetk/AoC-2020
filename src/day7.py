
def main(source):
    with open(source) as r:
        lines = r.readlines()
    ruleStrings = [x.split(' bags contain ') for x in lines]

    rules = {rule[0]: makeRule(rule[1]) for rule in ruleStrings}
    iRules = invertRules(rules)

    myBag = 'shiny gold'

    result1 = part1(iRules, myBag)
    print(result1)

    result2 = part2(rules, myBag)
    print(result2)


def makeRule(contentsString):
    contents = contentsString.split(', ')
    splittedContent = [c.split(' ') for c in contents]
    return {' '.join(c[1:3]): int(c[0]) for c in splittedContent if c[0].isdigit()}


def invertRules(rules):
    iRules = {}
    for rule, content in rules.items():
        for k, v in content.items():
            if k in iRules:
                iRules[k].append(rule)
            else:
                iRules[k] = [rule]
    return iRules


def bagsInBags1(rules, myBag):
    oldBags = set([myBag])
    c = set()
    while oldBags:
        newBags = set()
        for bag in oldBags:
            if bag in rules:
                for b in rules[bag]:
                    newBags.add(b)
                    c.add(b)
        oldBags = newBags
    return len(c)


def part1(iRules, myBag):
    return bagsInBags1(iRules, myBag)


def bagsInBags2(rules, bag):
    c = 0
    subBags = rules[bag]
    if subBags:
        for subBag, nr in subBags.items():
            c += nr + nr * bagsInBags2(rules, subBag)
    return c


def part2(rules, myBag):
    return bagsInBags2(rules, myBag)


if __name__ == '__main__':
    challenge = '7-1'
    source = fr'resources\day{challenge}.txt'
    main(source)
