with open("06/input.txt", "r") as f:
    line = f.read().strip()

for i in range(len(line)):
    # print(set(line[i:i+4]))
    if len(set(line[i : i + 14])) == 14:
        print(i + 14)
        break
