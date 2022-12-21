import re

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

monkeys = {}
todo = []
for line in lines:
    tokens = re.split(r":?\s", line)
    if len(tokens) == 2:
        monkeys[tokens[0]] = int(tokens[1])
    else:
        todo.append(tokens)

while "root" not in monkeys:
    for [result, a, op, b] in todo:
        if result in monkeys or a not in monkeys or b not in monkeys:
            continue
        a, b = monkeys[a], monkeys[b]
        if op == "+":
            monkeys[result] = int(a) + int(b)
        elif op == "-":
            monkeys[result] = int(a) - int(b)
        elif op == "*":
            monkeys[result] = int(a) * int(b)
        elif op == "/":
            monkeys[result] = int(a) / int(b)
print(monkeys["root"])

monkeys = {}
todo = {}
for line in lines:
    tokens = re.split(r":?\s", line)
    if tokens[0] == "humn":
        continue
    if len(tokens) == 2:
        monkeys[tokens[0]] = int(tokens[1])
    else:
        todo[tokens[0]] = tokens[1:]

while True:
    prev_len = len(monkeys)
    for result, [a, op, b] in todo.items():
        if result in monkeys or a not in monkeys or b not in monkeys:
            continue
        a, b = monkeys[a], monkeys[b]
        if op == "+":
            monkeys[result] = int(a) + int(b)
        elif op == "-":
            monkeys[result] = int(a) - int(b)
        elif op == "*":
            monkeys[result] = int(a) * int(b)
        elif op == "/":
            monkeys[result] = int(a) // int(b)
    if prev_len == len(monkeys):
        break

root = "root"
target = "humn"

[a, op, b] = todo[root]
if a in monkeys:
    needed = monkeys[a]
    root = b
else:
    needed = monkeys[b]
    root = a

while True:
    if root == "humn":
        print(needed)
        break
    [a, op, b] = todo[root]
    if op == "+":
        if a in monkeys:
            needed = needed - monkeys[a]
            root = b
        else:
            needed = needed - monkeys[b]
            root = a
    elif op == "-":
        if a in monkeys:
            needed = monkeys[a] - needed
            root = b
        else:
            needed = needed + monkeys[b]
            root = a
    elif op == "*":
        if a in monkeys:
            needed = needed // monkeys[a]
            root = b
        else:
            needed = needed // monkeys[b]
            root = a
    elif op == "/":
        if a in monkeys:
            needed = monkeys[a] // needed
            root = b
        else:
            needed = needed * monkeys[b]
            root = a