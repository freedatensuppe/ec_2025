with open("puzzle_input_2.txt", "r") as f:
    names, rules = f.read().strip().split("\n\n")

names = names.split(",")
rules = [r for r in rules.split("\n")]
rules_dict = {}
rules_dict = {key: val.split(",") for key, val in (item.split(" > ") for item in rules)}

print(rules_dict)

s = 0

for index, name in enumerate(names):
    possible = True
    for i, c in enumerate(name):
        if c in rules_dict and i < len(name) - 1:
            if name[i + 1] not in rules_dict[c]:
                possible = False
                break
    if possible:
        s += index + 1
        print(index, name)

print(s)
