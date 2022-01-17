def power():
    gammaRate = ''
    epsilonRate = ''

    with open('input.txt') as f:
        lines = f.readlines()

    buffer = [0] * len(lines[0])
    for line in lines:
        for i, char in enumerate(line):
            if char == '0':
                buffer[i] = buffer[i] - 1
            elif char == '1':
                buffer[i] = buffer[i] + 1

    for b in buffer:
        if b > 0:
            gammaRate += '1'
            epsilonRate += '0'
        elif b < 0:
            gammaRate += '0'
            epsilonRate += '1'

    power = int(gammaRate,2) * int(epsilonRate,2)
    print(power)

def life():
    with open('input.txt') as f:
        lines = f.readlines()

    oxygen = findRating(lines, 1, 0)
    co2 = findRating(lines, 0, 0)

    life = int(oxygen,2) * int(co2,2)
    print(life)
    

def findRating(binaryList, common, index):
    if len(binaryList) == 1:
        return binaryList[0]
    value = 0
    zero = []
    one = []
    for number in binaryList:
        if number[index] == '0':
            value -= 1
            zero.append(number)
        elif number[index] == '1':
            value += 1
            one.append(number)

    if value >= 0:
            r = one if common else zero
    else:
        r = zero if common else one
    
    return findRating(r, common, index+1)
    
    

if __name__ == '__main__':
    life()
