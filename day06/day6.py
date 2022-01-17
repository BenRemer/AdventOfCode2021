from multiprocessing import Pool

m = {}

def main():
    days = 256

    with open('input.txt') as f:
        lines = f.readlines()

    totalFish = []
    total = 0

    for line in lines:
        line = line.strip()
        fishList = line.split(',')

        for fish in fishList:
            totalFish.append(int(fish))

    with Pool(5) as p:
        fpool = []
        for fish in totalFish:
            r = p.apply_async(calculateFish, (fish, 0, days))
            fpool.append(r)
        for f in fpool:
            total += f.get()

    print(total)

def calculateFish(fish, day, maxDays):
    if (fish, maxDays - day) in m:
        return m[(fish, maxDays - day)]
    if day == maxDays:
        return 1
    if fish == 0:
        total = calculateFish(6, day+1, maxDays) + calculateFish(8, day+1, maxDays)
        m[(0, maxDays - day )] = total
        return total
    return calculateFish(fish-1, day+1, maxDays)

if __name__ == '__main__':
    main()