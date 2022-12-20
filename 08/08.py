import sys


def check_vis(grid, row, col):
    top = all(grid[r][col] < grid[row][col] for r in range(0, row))
    bottom = all(grid[r][col] < grid[row][col] for r in range(row + 1, len(grid)))
    left = all(grid[row][c] < grid[row][col] for c in range(0, col))
    right = all(grid[row][c] < grid[row][col] for c in range(col + 1, len(grid[row])))
    return top or bottom or left or right


def score(grid, row, col):
    top, bottom, left, right = 0, 0, 0, 0

    for r in reversed(range(0, row)):
        top += 1
        if grid[r][col] >= grid[row][col]:
            break

    for r in range(row + 1, len(grid)):
        bottom += 1
        if grid[r][col] >= grid[row][col]:
            break

    for c in reversed(range(0, col)):
        left += 1
        if grid[row][c] >= grid[row][col]:
            break

    for c in range(col + 1, len(grid[row])):
        right += 1
        if grid[row][c] >= grid[row][col]:
            break

    return top * bottom * left * right


with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

grid = [[int(c) for c in line] for line in lines]

visible = [check_vis(grid, r, c) for r in range(len(grid)) for c in range(len(grid[r]))]
print("part 1:", sum(visible))

scores = [score(grid, r, c) for r in range(len(grid)) for c in range(len(grid[r]))]
print("part 2:", max(scores))
