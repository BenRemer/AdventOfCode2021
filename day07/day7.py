def part1():
    crabs = []
    with open('input.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        for crab in line.split(','):
            crabs.append(int(crab))
    
    crabs.sort()

    if len(crabs) % 2 == 0:
        m1 = crabs[int(len(crabs) / 2 - 1)]
        m2 = crabs[int(len(crabs) / 2)]
        median = int((m1 + m2) / 2)
    else:
        median = crabs[int(len(crabs) / 2)]
    
    fuel = 0
    for crab in crabs:
        if crab < median:
            fuel += median - crab
        else:
            fuel += crab - median

    print(fuel)
    
def part2():
    crabs = []
    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        for crab in line.split(','):
            crabs.append(int(crab))
    
    avg = 0
    for crab in crabs:
        avg += crab
    avg /= len(crabs)
    if avg - int(avg) < 0.6:
        avg = round(avg)
        avg -= 1
    else:
        avg = round(avg)

    fuel = 0
    for crab in crabs:
        smaller = crab if crab <= avg else avg
        bigger = avg if crab <= avg else crab

        for i in range(bigger - smaller):
            fuel += i + 1
    
    print(fuel)


if __name__ == '__main__':
    part2()