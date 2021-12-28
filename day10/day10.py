def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for x in range(len(lines)):
        lines[x] = lines[x].strip()

    corruptPointsMap = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137
    }
    corruptTotal = 0
    completionPointsMap = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    completionTotals = []
    newInput = []
    
    for line in lines:
        corrupted = getCorruptChar(line)
        if corrupted:
            corruptTotal += corruptPointsMap[corrupted]
        else:
            newInput.append(line)
    print('Corrupt Total:', corruptTotal)

    for line in newInput:
        missingChars = completeLine(line)
        total = 0
        for char in missingChars:
            total *= 5
            total += completionPointsMap[char]
        completionTotals.append(total)
    completionTotals.sort()
    middleScore = completionTotals[int((len(completionTotals) - 1)/2)]
    print('Completion Total:', middleScore)

def completeLine(line):
    missingChars = ''
    m = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>'
    }
    o = []
    for char in line:
        if char in m:
            o.append(char)
        else:
            last = o.pop()
    for char in o:
        missingChars = m[char] + missingChars
    return missingChars
            


def getCorruptChar(line):
    m = {
        '[':']',
        '(':')',
        '{':'}',
        '<':'>'
    }
    o = []
    for char in line:
        if char in m:
            o.append(char)
        else:
            last = o.pop()
            if m[last] != char:
                return char
    return None


if __name__ == '__main__':
    main()