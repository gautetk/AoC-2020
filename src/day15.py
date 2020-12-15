
def main():
    
    numbers = [0,8,15,2,12,1,4]

    result1 = findNr(numbers, 2020)
    print(result1)

    result2 = findNr(numbers, 30000000)
    print(result2)


def findNr(numbers, maxN):
    numDict = {n: i for i, n in enumerate(numbers[:-1], start=1)}
    n = numbers[-1]
    for i in range(len(numbers), maxN):
        last = numDict.get(n)
        numDict[n] = i
        if last == None:
            n = 0
        else:
            n = i-last
    return n



if __name__ == '__main__':

    main()
