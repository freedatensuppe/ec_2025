import sys

sys.setrecursionlimit(3000)
topmap = []

with open("puzzle_input_3.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def ignite(topmap, r, c, ignited):
    ignited.add((r, c))
    for d in dirs:
        rn = r + d[0]
        cn = c + d[1]
        if cn >= cols or cn < 0 or rn >= rows or rn < 0:
            continue
        if topmap[r][c] >= topmap[rn][cn] and (rn, cn) not in ignited:
            ignite(topmap, rn, cn, ignited)


ignited_prev1 = set()
for r in range(rows):
    for c in range(cols):
        ignited1 = set()
        ignite(topmap, r, c, ignited1)
        if len(ignited1) > len(ignited_prev1):
            ignited_prev1 = ignited1

for r, c in ignited_prev1:
    topmap[r][c] = "X"


ignited_prev2 = set()
for r in range(rows):
    for c in range(cols):
        if topmap[r][c] != "X":
            ignited2 = set()
            ignite(topmap, r, c, ignited2)
            if len(ignited2) > len(ignited_prev2):
                ignited_prev2 = ignited2

for r, c in ignited_prev2:
    topmap[r][c] = "X"

ignited_prev3 = set()
for r in range(rows):
    for c in range(cols):
        if topmap[r][c] != "X":
            ignited3 = set()
            ignite(topmap, r, c, ignited3)
            if len(ignited3) > len(ignited_prev3):
                ignited_prev3 = ignited3

print(len(ignited_prev1), len(ignited_prev2), len(ignited_prev3))
print(len(ignited_prev1) + len(ignited_prev2) + len(ignited_prev3))
