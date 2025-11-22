topmap = []

with open("puzzle_input_1.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

ignited = set()


def ignite(topmap, r, c):
    ignited.add((r, c))
    for d in dirs:
        cn = c + d[1]
        rn = r + d[0]
        if cn >= cols or cn < 0 or rn < 0 or rn >= rows:
            continue
        if (rn, cn) not in ignited and topmap[rn][cn] <= topmap[r][c]:
            ignite(topmap, rn, cn)


ignite(topmap, 0, 0)
print(sorted(ignited))
for r, c in ignited:
    topmap[r][c] = "X"

for t in topmap:
    print(*t)

print(len(ignited))
