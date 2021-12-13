
class Measure:
    def main(self):
        increased = 0
        previous = None

        with open('input.txt') as f:
            lines = f.readlines()

        for line in lines:
            depth = int(line)
            if previous and depth > previous:
                increased += 1
            previous = depth

        print(increased)

    def window(self):
        increased = 0
        
        with open('input.txt') as f:
            lines = f.readlines()

        A = None
        B = None
        count = 0

        while True:
            A = get_count(lines,  count)
            B = get_count(lines, count + 1)

            if A < B:
                increased += 1

            count += 1
            
            if len(lines) <= count + 3:
                break

        print(increased)

def get_count(lines, count):
    return int(lines[count]) + int(lines[count + 1]) + int(lines[count + 2])
            
if __name__ == '__main__':
    measure = Measure()
    measure.window()
