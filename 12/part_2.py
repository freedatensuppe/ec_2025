import sys

sys.setrecursionlimit(3000)
topmap = []

with open("puzzle_input_2.txt", "r") as f:
    for line in f:
        word = []
        for w in line.strip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

ignited = set()


def ignite(topmap, r, c, ignited):
    ignited.add((r, c))
    for d in dirs:
        rn = r + d[0]
        cn = c + d[1]
        if cn >= cols or cn < 0 or rn >= rows or rn < 0:
            continue
        if topmap[r][c] >= topmap[rn][cn] and (rn, cn) not in ignited:
            ignite(topmap, rn, cn, ignited)
    return ignited


ignite(topmap, 0, 0, ignited)
first = ignited
ignited = set()
ignite(topmap, rows - 1, cols - 1, ignited)
print(len(first), len(ignited))
print(len(first) + len(ignited))
both = first.union(ignited)
print(len(both))
