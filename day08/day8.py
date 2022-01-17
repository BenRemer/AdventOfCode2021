def part1():
    with open('input.txt') as f:
        lines = f.readlines()
    inputs = []
    outputs = []
    for line in lines:
        line = line.strip()
        signal, output = line.split('|')
        inputs.append(signal.strip())
        outputs.append(output.strip())

    seen = 0
    switcher = {
        2: 1,
        4: 4,
        3: 7,
        7: 8,
    }
    for signal in outputs:
        numbers = signal.split(' ')
        for number in numbers:
            seen += 1 if switcher.get(len(number), None) else 0
    return seen

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
    
    total = 0

    for line in lines:
        total += int(calculateDislpays(line))

    return total

def calculateDislpays(line):
    total = ''
    line = line.strip()
    inputs, outputs = line.split('|')
    inputDisplays = inputs.strip().split(' ')
    outputDisplays = outputs.strip().split(' ')

    displayMap = {}
    numMap = {}
    letterMap = {}
    positionMap = {}
    sizeMapper = {
        2: 1,
        4: 4,
        3: 7,
        7: 8,
        }
    
    for signal in inputDisplays:
        size = len(signal)
        if size == 5 or size == 6:
            positionMap.setdefault(size, []).append(signal)
        else:
            n = sizeMapper.get(size, None)
            if not size in displayMap and n:
                numMap[n] = sortString(signal)
                displayMap[sortString(signal)] = n

    for letter in numMap[8]:
        if letter in numMap[1] and letter in numMap[4] and letter in numMap[7]:
            letterMap.setdefault('cf', []).append(letter)
        elif letter not in numMap[1] and letter not in numMap[4] and letter in numMap[7]:
            letterMap.setdefault('a', []).append(letter)
        elif letter not in numMap[1] and letter in numMap[4] and letter not in numMap[7]:
            letterMap.setdefault('bd', []).append(letter)
        else:
            letterMap.setdefault('eg', []).append(letter)

    for letter in letterMap['bd']:
        if letterInEach(letter, positionMap[5]):
            letterMap.setdefault('d', []).append(letter)
        else:
            letterMap.setdefault('b', []).append(letter)
            five = getStringWithLetter(letter, positionMap[5])
            displayMap[sortString(five)] = 5
            positionMap[5].remove(five)
    del letterMap['bd']

    for letter in letterMap['cf']:
        sixArray = positionMap[6]
        if letterInEach(letter, sixArray):
            letterMap.setdefault('f', []).append(letter)
        else:
            letterMap.setdefault('c', []).append(letter)
            six = getStringWithoutLetter(letter, sixArray)
            displayMap[sortString(six)] = 6
    del letterMap['cf']

    for letter in letterMap['eg']:
        sixArray = positionMap[6]
        if letterInEach(letter, sixArray):
            letterMap.setdefault('g', []).append(letter)
        else:
            letterMap.setdefault('e', []).append(letter)
            nine = getStringWithoutLetter(letter, sixArray)
            displayMap[sortString(nine)] = 9
    del letterMap['eg']

    for display in positionMap[6]:
        if letterMap['c'][0] in display and letterMap['e'][0] in display:
            displayMap[sortString(display)] = 0

    for display in positionMap[5]:
        if letterMap['e'][0] in display:
            displayMap[sortString(display)] = 2
        else:
            displayMap[sortString(display)] = 3

    for display in outputDisplays:
        total += str(displayMap[sortString(display)])
    return total

def letterInEach(letter, array):
    for i in range(len(array)):
        if letter not in array[i]:
            return False
    return True

def getStringWithLetter(letter, array):
    for i in range(len(array)):
        if letter in array[i]:
            return array[i]

def getStringWithoutLetter(letter, array):
    for i in range(len(array)):
        if letter not in array[i]:
            return array[i]


def sortString(string):
    sortedString = sorted(string)
    return ''.join(sortedString)


if __name__ == '__main__':
    # total = part1()
    total = part2()
    print(total)