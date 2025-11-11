with open("puzzle_input_2.txt", "r") as f:
    knights = f.read().strip()


print(knights)

# knights = "ABabACacBCbca"

s = 0

for i, _ in enumerate(knights):
    if knights[i] == "a":
        s += knights[:i].count("A")
    if knights[i] == "b":
        s += knights[:i].count("B")
    if knights[i] == "c":
        s += knights[:i].count("C")

print(s)
