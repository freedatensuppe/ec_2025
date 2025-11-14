with open("puzzle_input_1.txt", "r") as f:
    names, rules = f.read().strip().split("\n\n")

names = names.split(",")
rules = [r for r in rules.split("\n")]
rules_dict = {}
rules_dict = {key: val.split(",") for key, val in (item.split(" > ") for item in rules)}

print(rules_dict)

for name in names:
    possible = True
    for i, c in enumerate(name):
        if c in rules_dict:
            if name[i + 1] not in rules_dict[c]:
                possible = False
                break
    if possible:
        print(name)
