scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

wins = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

losses = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

ties = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

def part1(lines):
    score = 0
    for line in lines:
        line = line.strip()
        [you, me] = line.split()
        score += scores[me]
        if wins[you] == me:
            score += 6
        elif ties[you] == me:
            score += 3
        elif losses[you] == me:
            score += 0
    print(score)

def part2(lines):
    score = 0
    for line in lines:
        line = line.strip()
        [you, result] = line.split()
        # lose
        if result == 'X':
            me = losses[you]
            score += 0
        elif result == 'Y':
            me = ties[you]
            score += 3
        elif result == 'Z':
            me = wins[you]
            score += 6
        score += scores[me]
    print(score)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    part1(lines)
    part2(lines)