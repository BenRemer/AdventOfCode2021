def vents():
    with open('input.txt') as f:
        lines = f.readlines()
    size = 1000
    array = [[0] * size for i in range(size)]

    for line in lines:
        line = line.strip().replace('->', ',').replace(' ', '')
        numbers = line.split(',')
        x1 = int(numbers[0])
        y1 = int(numbers[1])
        x2 = int(numbers[2])
        y2 = int(numbers[3])

        if x1 == x2:
            row = y1 if y1 <= y2 else y2
            end = y2 if y2 > y1 else y1
            array = updateCol(array, row, x1, end)
        elif y1 == y2:
            col = x1 if x1 <= x2 else x2
            end = x2 if x2 > x1 else x1
            array = updateRow(array, y1, col, end)
        else:
            array = updateDiagonal(array, x1, y1, x2, y2)

    # printArray(array)

    total = 0
    for line in array:
        for number in line:
            if number >= 2:
                total += 1
    print(total)


def updateDiagonal(array, x1, y1, x2, y2):
    if x1 <= x2:
        while x1 <= x2:
            array[y1][x1] += 1
            x1 += 1
            y1 += 1 if y1 < y2 else -1
    else:
        while x2 <= x1:
            array[y2][x2] += 1
            x2 += 1
            y2 -= 1 if y2 > y1 else -1

    return array

def updateRow(array, row, col, end):
    while col <= end:
        array[row][col] += 1
        col += 1
    return array

def updateCol(array, row, col, end):
    while row <= end:
        array[row][col] += 1
        row += 1
    return array

def printArray(array):
    for line in array:
        print(line)

if __name__ == '__main__':
    vents()