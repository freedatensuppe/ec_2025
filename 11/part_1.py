with open("test_input_1.txt", "r") as f:
    ducks = [int(i) for i in f.read().strip().split("\n")]

duck_moved = True
print(ducks)

count = 0

while duck_moved:
    duck_moved = False
    for i, _ in enumerate(ducks[:-1]):
        if ducks[i + 1] < ducks[i]:
            ducks[i] -= 1
            ducks[i + 1] += 1
            duck_moved = True
    if duck_moved:
        count += 1

print(ducks, count)

duck_moved = True

while duck_moved:
    duck_moved = False
    for i, _ in enumerate(ducks[:-1]):
        if ducks[i] < ducks[i + 1]:
            ducks[i + 1] -= 1
            ducks[i] += 1
            duck_moved = True
    if duck_moved:
        count += 1
    if count == 10:
        break


print(ducks, count)
checksum = sum([(i + 1) * duck for i, duck in enumerate(ducks)])
print(checksum)
