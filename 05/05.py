import re

with open("05/input.txt", "r") as f:
    lines = f.read().splitlines()


class Stacks:
    stacks = []

    def __init__(self, num_stacks):
        self.stacks = []
        for i in range(num_stacks):
            self.stacks.append([])

    def add(self, item, stack):
        self.stacks[stack].append(item)

    def move_one(self, from_index, to_index):
        item = self.stacks[from_index].pop()
        self.stacks[to_index].append(item)

    def move_many(self, from_index, to_index, num):
        items = self.stacks[from_index][-num:]
        self.stacks[from_index] = self.stacks[from_index][:-num]
        self.stacks[to_index].extend(items)

    def top_of_each(self):
        return ''.join(stack[-1] for stack in self.stacks)


split = lines.index("")
stack_data = lines[:split]
num_stacks = int(stack_data[-1].split()[-1])
stack_data = stack_data[:-1]

stacks = Stacks(num_stacks)

for stack in range(num_stacks):
    for depth in reversed(range(len(stack_data))):
        item = stack_data[depth][stack * 4 + 1]
        if item != " ":
            stacks.add(item, stack)


instructions = lines[split + 1 :]
parser = re.compile(r"move (\d+) from (\d+) to (\d+)")
for instruction in instructions:
    match = parser.match(instruction)
    if match:
        [num, from_index, to_index] = list(map(int, match.groups()))
        # for _ in range(num):
        #     stacks.move_one(from_index - 1, to_index - 1)
        stacks.move_many(from_index - 1, to_index - 1, num)

print(stacks.top_of_each())