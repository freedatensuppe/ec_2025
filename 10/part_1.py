topmap = []

with open("puzzle_input_1.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

print(topmap)

cols = len(topmap[0])
rows = len(topmap)

dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

for i in range(len(topmap)):
    for j in range(len(topmap[0])):
        if topmap[i][j] == "D":
            start = (i, j)


def take_step(topmap, r, c, n, sheep):
    if n == 5:
        return
    if topmap[r][c] == "S":
        sheep.add((r, c))
    for d in dirs:
        cn = c + d[1]
        rn = r + d[0]
        if cn >= cols or cn < 0 or rn < 0 or rn >= rows:
            continue
        else:
            take_step(topmap, rn, cn, n + 1, sheep)


sheep = set()
take_step(topmap, start[0], start[1], 0, sheep)

print(len(sheep))
