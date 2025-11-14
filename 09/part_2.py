from itertools import combinations

with open("puzzle_input_2.txt", "r") as f:
    genes = []
    for line in f:
        genes.append(line.strip().split(":")[1])


def find_child(child, parents):
    for i, _ in enumerate(child):
        if not (child[i] == parents[0][i] or child[i] == parents[1][i]):
            return False
    return True


def similarity(child, parents):
    s1 = 0
    s2 = 0
    for i, _ in enumerate(child):
        if child[i] == parents[0][i]:
            s1 += 1
        if child[i] == parents[1][i]:
            s2 += 1
    print(s1, s2)
    return s1 * s2


score = 0

for i, gene in enumerate(genes):
    parents = list(set(genes) - set([gene]))
    for c in combinations(parents, 2):
        if find_child(gene, c):
            score += similarity(gene, c)

print(score)
