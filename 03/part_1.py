with open("puzzle_input.txt", "r") as f:
    crates = [int(i) for i in f.read().strip().split(",")]


print(crates)
s = sum(set(sorted(crates)))
print(s)
