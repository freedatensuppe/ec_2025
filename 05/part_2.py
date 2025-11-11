with open("puzzle_input_2.txt", "r") as f:
    swords = []
    for line in f:
        a, s = line.strip().split(":")
        swords.append(s.split(","))

qualities = []

for numbers in swords:
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
    quality = int("".join([str(s[1]) for s in sword if any(s)]))
    qualities.append(quality)

result = max(qualities) - min(qualities)

print(result)
