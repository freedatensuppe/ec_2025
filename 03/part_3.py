with open("puzzle_input3.txt", "r") as f:
    crates = [int(i) for i in f.read().strip().split(",")]

unique_crates = list(set(sorted(crates)))
counts = []

for i in unique_crates:
    counts.append(crates.count(i))


print(sorted(counts))
print(sorted(counts)[-1])
