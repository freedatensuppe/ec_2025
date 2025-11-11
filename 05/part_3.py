with open("puzzle_input_3.txt", "r") as f:
    swords = []
    for line in f:
        a, s = line.strip().split(":")
        swords.append(s.split(","))

qualities = []
swort_trees = []

for z, numbers in enumerate(swords):
    sword = 0
    sword = [[0, 0, 0] for _ in range(len(numbers))]
    quality_ext = 0
    for n in numbers:
        for s in sword:
            if all(s):
                continue
            if s[1] == 0:
                s[1] = n
                break
            elif n < s[1] and s[0] == 0:
                s[0] = n
                break
            elif n > s[1] and s[2] == 0:
                s[2] = n
                break
            else:
                continue
    sword_tree = [s for s in sword if any(s)]
    swort_trees.append(sword_tree)
    quality = int("".join([str(s[1]) for s in sword if any(s)]))
    quality_ext = [int("".join(map(str, s)).replace("0", "")) for s in sword if any(s)]
    qualities.append([quality, quality_ext, z + 1])

qualities.sort(reverse=True)

result = sum([(i + 1) * q[2] for i, q in enumerate(qualities)])
print(result)
