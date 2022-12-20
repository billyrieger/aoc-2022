with open("input.txt", "r") as f:
    lines = f.read().splitlines()

all_dir_sizes = []
filesystem = [0]

for command in lines:
    match command.split():
        case ["$", "cd", dir]:
            match dir:
                case "/":
                    filesystem = [0]
                case "..":
                    subdir = filesystem.pop()
                    all_dir_sizes.append(subdir)
                    filesystem[-1] += subdir
                case _:
                    filesystem.append(0)

        case ["$", "ls"] | ["dir", _]:
            pass

        case [size, _]:
            filesystem[-1] += int(size)

while len(filesystem) > 1:
    subdir = filesystem.pop()
    all_dir_sizes.append(subdir)
    filesystem[-1] += subdir

all_dir_sizes.append(filesystem[0])

print("part 1:", sum(size for size in all_dir_sizes if size < 100000))

total_space = 70000000
needed_free = 30000000
current_used = sum(filesystem)
min_to_remove = needed_free - (total_space - current_used)
print("part 2:", min(size for size in all_dir_sizes if min_to_remove <= size))
