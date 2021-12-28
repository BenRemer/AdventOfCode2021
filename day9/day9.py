def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for x in range(len(lines)):
        lines[x] = lines[x].strip()

    global sizeX
    global sizeY
    sizeX = len(lines[0])
    sizeY= len(lines)

    points = {}
    basin = {}
    y = 0
    x = 0

    for j in range(sizeY):
        for i in range(sizeX):
            smallest, newX, newY = _findSmallest(x, y, lines)
            points[(newX,newY)] = smallest
            if int(lines[y][x]) != 9:
                basin[(newX,newY)] = basin.setdefault((newX, newY), 0) + 1
            x += 1
        x = 0
        y += 1
        
    risk = 0
    for key, value in points.items():
        risk += 1 + value
    print('risk:', risk)
    
    largestBasins = []
    lBasin = 1
    for key, value in basin.items():
        largestBasins.append(value)
    largestBasins.sort(reverse=True)
    for i in range(3):
        lBasin *= largestBasins[i]
    print('largest 3 basin:', lBasin)

def _findSmallest(x, y, lines):
    start = int(lines[y][x])
    left = int(lines[y][x-1]) if x-1 >= 0 else -1
    right = int(lines[y][x+1]) if x+1 < sizeX else -1
    up = int(lines[y-1][x]) if y-1 >= 0 else -1
    down = int(lines[y+1][x]) if y+1 < sizeY else -1
    l = [left, right, up, down, start]
    m = l.index(min([i for i in l if i >= 0]))

    if m == 0:  # left
        return _findSmallest(x-1, y, lines)
    elif m == 1:  # right
        return _findSmallest(x+1, y, lines)
    elif m == 2:  # up
        return _findSmallest(x, y-1, lines)
    elif m == 3:  # down
        return _findSmallest(x, y+1, lines)
    else:
        return start, x, y

if __name__ == '__main__':
    main()