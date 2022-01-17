def bingo():
    with open('input.txt') as f:
        lines = f.readlines()
    
    numBoards = int((len(lines) - 1) / 6)

    bingoNumbers = lines[0].strip().split(',')

    arrays = [[[0] * 5 for i in range(5)] for x in range(numBoards)]
    hmap = {}
    row = 0
    col = 0
    board = -1
    won = []

    for i, line in enumerate(lines):
        line = line.strip()
        if line == '':
            row = 0
            board += 1
        elif i != 0:
            col = 0
            line = line.replace('  ', ' ')
            numbers = line.split(' ')
            for number in numbers:
                number = int(number)
                arrays[board][row][col] = number
                hmap.setdefault(number, []).append([board, row, col])
                col += 1
            row += 1
                
    for n in bingoNumbers:
        n = int(n)
        if n in hmap:
            locations = hmap[n]
            for location in locations:
                board, row, col = location
                arrays[board][row][col] = -1
                if board not in won and checkForWin(arrays[board]):
                    won.append(board)
                    if len(won) == numBoards:
                        return calculateScore(arrays[board], n)

def checkForWin(board):
    for line in board:
        total = 0
        for number in line:
            total += number
        if total == -5:
            return True
    
    for col in range(5):
        total = 0
        for row in range(5):
            total += board[row][col]
        if total == -5:
            return True
    return False

def calculateScore(board, multiplyer):
    print(multiplyer)
    total = 0
    for line in board:
        for number in line:
            if number > -1:
                total += number
    return total * multiplyer

if __name__ == '__main__':
    score = bingo()
    print('Score: ', score)