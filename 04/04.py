import re, sys

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

part1, part2 = 0, 0
for line in lines:
    [a0, a1, b0, b1] = list(map(int, re.split(r",|\-", line)))
    if (a0 <= b0 and b1 <= a1) or (b0 <= a0 and a1 <= b1):
        part1 += 1
    if (a0 <= b0 <= a1) or (b0 <= a0 <= b1):
        part2 += 1
print("part 1:", part1)
print("part 2:", part2)
