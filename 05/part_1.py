with open("puzzle_input_1.txt", "r") as f:
    nums = f.read().strip().split(",")

inds, first = [i for i in nums[0].split(":")]
numbers = [int(first)] + [int(i) for i in nums[1:]]

print(inds, first, numbers)

sword = [[0, 0, 0] for _ in range(len(numbers))]

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

print("".join([str(s[1]) for s in sword if any(s)]))
