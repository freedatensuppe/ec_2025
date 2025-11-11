with open("puzzle_input.txt", "r") as f:
    knights = f.read().strip()


print(knights)

# knights = "ABabACacBCbca"

s = 0

for i, _ in enumerate(knights):
    if knights[i] == "a":
        s += knights[:i].count("A")

print(s)
