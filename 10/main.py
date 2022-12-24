import sys

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()


def part1():
    cycle, x, strength = 0, 1, 0

    def step():
        nonlocal cycle, strength
        cycle += 1
        if cycle % 40 == 20:
            strength += cycle * x

    for command in lines:
        match command.split():
            case ["noop"]:
                step()
            case ["addx", num]:
                step()
                step()
                x += int(num)

    print("part 1:", strength)


def part2():
    cycle, x = 0, 1

    def step():
        nonlocal cycle
        print("#" if x - 1 <= cycle % 40 <= x + 1 else " ", end="")
        cycle += 1
        if cycle % 40 == 0:
            print()

    print("part 2:")
    for command in lines:
        match command.split():
            case ["noop"]:
                step()
            case ["addx", num]:
                step()
                step()
                x += int(num)


part1()
part2()
