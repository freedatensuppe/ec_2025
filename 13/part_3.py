from collections import deque

with open("puzzle_input_3.txt", "r") as f:
    locks = deque([1])
    for i, lock in enumerate(f.read().strip().split("\n")):
        print(i)
        a, b = list(map(int, lock.split("-")))
        if i % 2 == 0:
            for x in range(a, b + 1):
                locks.append(x)
        if i % 2 == 1:
            for x in range(a, b + 1):
                locks.appendleft(x)


ind = locks.index(1)
pos = 202520252025 % len(locks)
print(locks[(ind + pos) % len(locks)])
