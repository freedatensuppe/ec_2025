import itertools

topmap = []

with open("puzzle_input_2.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)
hideouts = set()
sheep_init = set()
dragon_pos = []
sheep = set()

dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

for i in range(len(topmap)):
    for j in range(len(topmap[0])):
        if topmap[i][j] == "D":
            start = (i, j)
        if topmap[i][j] == "#":
            hideouts.add((i, j))
        if topmap[i][j] == "S":
            sheep_init.add((i, j))


def take_step(r, c):
    pos = []
    for d in dirs:
        cn = c + d[1]
        rn = r + d[0]
        if cn >= cols or cn < 0 or rn < 0 or rn >= rows:
            continue
        pos.append((rn, cn))
    return pos


dragon_pos.append(start)

print("initial number of sheep:", len(sheep_init))
print(30 * "-")

sheep = sheep_init
# print(sorted(sheep_init))

for k in range(20):
    new_pos = [take_step(pos[0], pos[1]) for pos in dragon_pos]
    new_pos = set(itertools.chain.from_iterable(new_pos))

    sheep = sheep - (new_pos - hideouts)
    sheep = {(i + 1, j) for (i, j) in sheep}

    sheep = sheep - (new_pos - hideouts)

    dragon_pos = new_pos

    print(f"Sheep eaten after cycle {k + 1}:", len(sheep_init) - len(sheep))
