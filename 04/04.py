with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    part1 = 0
    part2 = 0
    for line in lines:
        [a, b] = line.split(",")
        [a0, a1] = list(map(int, a.split("-")))
        [b0, b1] = list(map(int, b.split("-")))
        if (a0 <= b0 and b1 <= a1) or (b0 <= a0 and a1 <= b1):
            part1 += 1
        if (a0 <= b0 <= a1) or (b0 <= a0 <= b1):
            part2 += 1
    print("part 1:", part1)
    print("part 2:", part2)
