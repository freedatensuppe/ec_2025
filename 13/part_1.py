from collections import deque

with open("puzzle_input_1.txt", "r") as f:
    locks = deque([1])
    for i, lock in enumerate(f.read().strip().split("\n")):
        if i % 2 == 0:
            locks.append(int(lock))
        if i % 2 == 1:
            locks.appendleft(int(lock))


ind = locks.index(1)
locks.rotate(-ind)
print(locks)
pos = 2025 % len(locks)
print(locks[pos])
