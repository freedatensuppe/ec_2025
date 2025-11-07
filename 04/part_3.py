with open("puzzle_input3.txt", "r") as f:
    gears = f.read().strip().split("\n")

i = 1

for g in gears[1:-1]:
    if "|" in g:
        a, b = g.split("|")
        i *= int(b) / int(a)

rot = i * 100 * int(gears[0]) / int(gears[-1])

print(int(rot))
