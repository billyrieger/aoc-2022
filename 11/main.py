import copy, math, re, sys


class Monkey:
    def __init__(self, items, operation, div_test, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.div_test = div_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspected = 0

    def eval(self, old):
        result = self.operation[:]
        result.replace("old", f"{old}")
        return int(eval(result))

    def inspect(self, divide_by_three):
        item = self.items.pop(0)
        new_item = self.eval(item)
        if divide_by_three:
            new_item = new_item // 3
        self.inspected += 1
        if new_item % self.div_test == 0:
            return (new_item, self.true_monkey)
        else:
            return (new_item, self.false_monkey)


def simulate(monkeys, rounds, divide_by_3):
    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                (item, pass_to) = monkey.inspect(divide_by_3)
                if divide_by_3:
                    monkeys[pass_to].items.append(item)
                else:
                    monkeys[pass_to].items.append(item % global_mod)

    inspections = [monkey.inspected for monkey in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


with open(sys.argv[1], "r") as f:
    file = f.read()

regex = re.compile(
    r"""Monkey \d+:
  Starting items: (.*)
  Operation: new = (.*)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
)

matches = regex.findall(file)
monkeys = []
for (items, operation, div_test, true_monkey, false_monkey) in matches:
    items = list(map(int, re.split(r", ", items)))
    monkey = Monkey(
        items, operation, int(div_test), int(true_monkey), int(false_monkey)
    )
    monkeys.append(monkey)

global_mod = math.prod(monkey.div_test for monkey in monkeys)

print("part 1:", simulate(copy.deepcopy(monkeys), 20, True))
print("part 2:", simulate(monkeys, 10000, False))