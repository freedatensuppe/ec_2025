x, y = 25, 9


def add_num(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


def mul_num(x1, y1, x2, y2):
    return (
        x1 * x2 - y1 * y2,
        x1 * y2 + y1 * x2,
    )


def div_num(x1, y1, x2, y2):
    return x1 // x2, y1 // y2


r1, r2 = 0, 0

for i in range(3):
    r1, r2 = mul_num(r1, r2, r1, r2)
    r1, r2 = div_num(r1, r2, 10, 10)
    r1, r2 = add_num(r1, r2, x, y)
    print(r1, r2)
