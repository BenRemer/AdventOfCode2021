def main():
    global SIZE
    SIZE = 10
    with open('input.txt') as f:
        lines = f.readlines()
    octopi = convertToOctopi(lines)
    
    numberOfSteps = 100

    # totalFlashes = calculateFlashes(octopi, numberOfSteps)
    
    # print('Total Flashes for {} steps: {}'.format(numberOfSteps, totalFlashes))

    stepsToSync = calculateSyncFlash(octopi)

    print('{} steps until complete flash'.format(stepsToSync))

def calculateSyncFlash(octopi):
    steps = 0
    while True:
        steps += 1
        octopi = increaseEnergyLevel(octopi)
        octopi, numOfFlashes = flashOctopi(octopi)
        octopi = updateFlashed(octopi)
        if numOfFlashes == 100:
            break
    return steps

def calculateFlashes(octopi, numberOfSteps):
    totalFlashes = 0
    for i in range(numberOfSteps):
        # printOcto(octopi)
        octopi = increaseEnergyLevel(octopi)
        octopi, numOfFlashes = flashOctopi(octopi)
        octopi = updateFlashed(octopi)
        totalFlashes += numOfFlashes
    return totalFlashes
    
def updateFlashed(octopi):
    for y in range(SIZE):
        for x in range(SIZE):
            if octopi[y][x] > 9:
                octopi[y][x] = 0
    return octopi

def increaseEnergyLevel(octopi):
    for j in range(SIZE):
        for i in range(SIZE):
            octopi[j][i] += 1
    return octopi

def flashOctopi(octopi):
    flashed = []
    while True:
        sawFlash = False
        for j in range(SIZE):
            for i in range(SIZE):
                if octopi[j][i] > 9 and (i,j) not in flashed:
                    sawFlash = True
                    flashed.append((i,j))
                    octopi = flashNearby(octopi, i, j)
        if not sawFlash:
            break
    return octopi, len(flashed)

def flashNearby(octopi, x, y):
    if x-1 >= 0:  # left
        octopi[y][x-1] += 1
    if x+1 < SIZE:  # right
        octopi[y][x+1] += 1 
    if y-1 >= 0:  # up
        octopi[y-1][x] += 1 
    if y+1 < SIZE:  # down
        octopi[y+1][x] += 1 
    if x-1 >= 0 and y-1 >= 0:  # dLeftUp
        octopi[y-1][x-1] += 1 
    if x+1 < SIZE and y-1 >= 0:  # dRightUp
        octopi[y-1][x+1] += 1 
    if x-1 >= 0 and y+1 < SIZE:  # dLeftDown
        octopi[y+1][x-1] += 1 
    if x+1 < SIZE and y+1 < SIZE:  # dRightDown
        octopi[y+1][x+1] += 1 
    return octopi

def convertToOctopi(lines):
    octopi = []
    for line in lines:
        l = []
        line = line.strip()
        for char in line:
            l.append(int(char))
        octopi.append(l)
    return octopi

def printOcto(octopi):
    for line in octopi:
        m = ''
        for i in line:
            m = m + str(i)
        print(m)
    print('----')

if __name__ == '__main__':
    main()