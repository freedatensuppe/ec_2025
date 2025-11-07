with open("puzzle_input.txt", "r") as f:
    names, coords = f.read().strip().replace("R", "").replace("L", "-").split("\n\n")

names = names.split(",")
coords = coords.split(",")

current = 0

for c in coords:
    current = current + int(c)
    if current < 0:
        current = 0
    if current >= len(names):
        current = len(names) - 1

print(names[current])
