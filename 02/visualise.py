import matplotlib.pyplot as plt
import numpy as np

#  x, y = 21763, -68997


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


iterations = []
count = 0

for p in points:
    good = True
    r1, r2 = 0, 0
    iteration = 0
    for i in range(100):
        r1, r2 = mul_num(r1, r2, r1, r2)
        r1, r2 = div_num(r1, r2, 100000, 100000)
        r1, r2 = add_num(r1, r2, p[0], p[1])
        iteration += 1
        if abs(r1) > 1000000 or abs(r2) > 1000000:
            good = False
            break
    iterations.append(iteration)


iterations_2d = np.array(iterations).reshape(1001, 1001)
print(iterations_2d.min())
print(iterations_2d.max())

img = plt.imshow(
    iterations_2d, origin="lower", cmap="Spectral", extent=(x, x + 1000, y, y + 1000)
)
img.axes.get_xaxis().set_visible(False)
img.axes.get_yaxis().set_visible(False)
plt.savefig("my_grid.png", bbox_inches="tight", pad_inches=0)
plt.imsave("my_grid2.png", iterations_2d, format="png", cmap="hot")
