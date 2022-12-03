import os

def priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    elif ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27
    else:
        return 0


def part1(rucksacks):
    total = 0
    for rucksack in rucksacks:
        half_len = len(rucksack) // 2
        compartment0, compartment1 = rucksack[:half_len], rucksack[half_len:]
        common_items = list(set(compartment0) & set(compartment1))
        assert len(common_items) == 1, 'exactly one misplaced item per rucksack'
        total += priority(common_items[0])
    print('part 1:', total)


def part2(rucksacks):
    total = 0
    groups = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
    for [a, b, c] in groups:
        common_items = list(set(a) & set(b) & set(c))
        assert len(common_items) == 1, 'exactly one common item per group'
        total += priority(common_items[0])
    print('part 2:', total)


with open(os.path.join('03', 'test.txt'), 'r') as f:
    rucksacks = f.read().splitlines()
    part1(rucksacks)
    part2(rucksacks)