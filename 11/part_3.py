with open("puzzle_input_3.txt", "r") as f:
    ducks = [int(i) for i in f.read().strip().split("\n")]

# duck_moved = True
#
# count = 0
#
# while duck_moved:
#     duck_moved = False
#     for i, _ in enumerate(ducks[:-1]):
#         if ducks[i] < ducks[i + 1]:
#             ducks[i + 1] -= 1
#             ducks[i] += 1
#             duck_moved = True
#     if duck_moved:
#         count += 1
#
# print(ducks, count)

mean = sum(ducks) / len(ducks)
rounds = [mean - duck for duck in ducks if duck < mean]
print(sum(rounds))
