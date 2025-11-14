with open("puzzle_input_1.txt", "r") as f:
    coords = list(map(int, f.read().strip().split(",")))

num_coords = 32
count = 0

for i, c in enumerate(coords):
    if abs(coords[i] - coords[i - 1]) == num_coords / 2:
        count += 1


print(count)
