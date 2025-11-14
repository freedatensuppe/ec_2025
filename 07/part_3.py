with open("puzzle_input_3.txt", "r") as f:
    names, rules = f.read().strip().split("\n\n")

names = names.split(",")
rules = [r for r in rules.split("\n")]
rules_dict = {}
rules_dict = {key: val.split(",") for key, val in (item.split(" > ") for item in rules)}


def check_name(name):
    possible = True
    for i, c in enumerate(name):
        if c in rules_dict and i < len(name) - 1:
            if name[i + 1] not in rules_dict[c]:
                possible = False
                break
    return possible


def extend_name(name, name_list, rules_dict):
    if len(name) == 11:
        return
    if name[-1] in rules_dict:
        for c in rules_dict[name[-1]]:
            new_name = name + c
            if len(new_name) >= 7:
                name_list.append(new_name)
            extend_name(new_name, name_list, rules_dict)


name_list = []
for name in names:
    if check_name(name):
        extend_name(name, name_list, rules_dict)

print(len(set(name_list)))
