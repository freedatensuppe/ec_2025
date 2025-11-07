with open("puzzle_input2.txt", "r") as f:
    names, coords = f.read().strip().replace("R", "").replace("L", "-").split("\n\n")

names = names.split(",")
coords = coords.split(",")

current = 0

for c in coords:
    current = (current + int(c)) % len(names)

print(names[current])
