x, y = 35300, -64910


def add_num(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


def mul_num(x1, y1, x2, y2):
    return (
        x1 * x2 - y1 * y2,
        x1 * y2 + y1 * x2,
    )


def div_num(x1, y1, x2, y2):
    return int(x1 / x2), int(y1 / y2)


coord_x, coord_y = add_num(x, y, 1000, 1000)
print(x, y)
print(coord_x, coord_y)

points = []

for j in range(1001):
    for i in range(1001):
        points.append((x + i, y + j))

print(points[:5])
print(points[-5:])

print(len(points))

good_points = []
results = []
count = 0

for p in points:
    good = True
    r1, r2 = 0, 0
    for i in range(100):
        r1, r2 = mul_num(r1, r2, r1, r2)
        r1, r2 = div_num(r1, r2, 100000, 100000)
        r1, r2 = add_num(r1, r2, p[0], p[1])
        if abs(r1) > 1000000 or abs(r2) > 1000000:
            good = False
            break
    if good:
        good_points.append(p)
        results.append((r1, r2))
        count += 1

print(good_points[:5])
print(results[:5])
print()
print(good_points[-5:])
print(results[-5:])
print(len(good_points))

print(count)
