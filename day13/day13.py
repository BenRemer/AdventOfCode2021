
def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    cords = []
    folds = []
    fold = False
    xRange = 0
    yRange = 0


    for line in lines:
        if not line:
            fold = True
        elif fold:
            words = line.split(' ')
            folds.append(words[-1])
        else:
            x,y = line.split(',')
            c = (int(x), int(y))
            cords.append(c)
            if int(x) > xRange:
                xRange = int(x)
            if int(y) > yRange:
                yRange = int(y)
    
    array = [['.' for x in range(xRange + 1)] for y in range(yRange + 1)]
    
    for c in cords:
        x,y = c
        array[y][x] = '#'

    for f in folds:
        axis, position = f.split('=')
        position = int(position)
        if axis == 'y':
            for y in range(position, yRange + 1):
                for x in range(xRange + 1):
                    if array[y][x] == '#':
                        array[position * 2 - y][x] = array[y][x]
                    array[y][x] = None
        else:
            for x in range(position, xRange + 1):
                for y in range(yRange + 1):
                    if array[y][x] == '#':
                        array[y][position * 2 - x] = array[y][x]
                    array[y][x] = None
                        

    count = 0
    for line in array:
        seen = False
        for item in line:
            if item:
                seen = True
                print(item, end=' ')
        if seen:
            print()
    

if __name__ == '__main__':
    main()