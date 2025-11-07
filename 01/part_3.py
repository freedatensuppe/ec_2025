with open("test_input.txt", "r") as f:
    names, coords = f.read().strip().replace("R", "").replace("L", "-").split("\n\n")

names = names.split(",")
coords = coords.split(",")

for c in coords:
    c = int(c) % len(names)
    names[0], names[c] = names[c], names[0]

print(names[0])
