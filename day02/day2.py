
def calculate():
    horizontal = 0
    depth = 0
    aim = 0

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        command, number = line.split(' ')

        if command == 'forward':
            horizontal += int(number)
            depth += aim * int(number)
        elif command == 'down':
            aim += int(number)
        elif command == 'up':
            aim -= int(number)
        else:
            pass
    return horizontal * depth


if __name__ == '__main__':
    print(calculate())

