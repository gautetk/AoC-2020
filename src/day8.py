
def main(source):
    with open(source) as r:
        lines = r.readlines()
    instructions = [x.rstrip('\n').split(' ') for x in lines]

    result1 = part1(instructions)
    print(result1)

    result2 = part2(instructions)
    print(result2)


def execute(instruction):
    operation, argument = instruction
    if operation == 'acc':
        return int(argument), 1
    elif operation == 'jmp':
        return 0, int(argument)
    elif operation == 'nop':
        return 0, 1


def runProgram(instructions):
    acc = 0
    usedInstructions = set()
    instruction = 0
    while instruction not in usedInstructions:
        usedInstructions.add(instruction)
        deltaAcc, deltainstruction = execute(instructions[instruction])
        acc += deltaAcc
        instruction += deltainstruction
        if instruction >= len(instructions):
            return acc, True

    return acc, False


def part1(instructions):
    acc, _ = runProgram(instructions)
    return acc


def changeInstruction(i, instructions):
    operation, argument = instructions[i]
    if operation == 'acc':
        return False
    elif operation == 'jmp':
        return instructions[:i] + [['nop', argument]] + instructions[i+1:]
    elif operation == 'nop':
        return instructions[:i] + [['jmp', argument]] + instructions[i+1:]


def part2(instructions):
    changeLine = 0
    for i in range(len(instructions)):
        newInstructions = changeInstruction(i, instructions)
        if newInstructions:
            acc, success = runProgram(newInstructions)
            if success:
                return acc


if __name__ == '__main__':
    challenge = '8-1'
    source = fr'resources\day{challenge}.txt'
    main(source)
