with open("puzzle_input2.txt", "r") as f:
    crates = [int(i) for i in f.read().strip().split(",")]


print(list(sorted(set(crates)))[:20])
s = sum(list(sorted(set(crates)))[:20])
print(s)
