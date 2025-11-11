with open("puzzle_input_3.txt", "r") as f:
    knights = f.read().strip()


knights = knights * 1000


# knights = "AABCBABCABCabcabcABCCBAACBCa"
# knights = "AABCBABCABCabcabcABCCBAACBCaAABCBABCABCabcabcABCCBAACBCa"


s = 0

for i, _ in enumerate(knights):
    if i < 1000:
        if knights[i] == "a":
            s += knights[: i + 1001].count("A")
        if knights[i] == "b":
            s += knights[: i + 1001].count("B")
        if knights[i] == "c":
            s += knights[: i + 1001].count("C")
    else:
        if knights[i] == "a":
            s += knights[i - 1000 : i + 1001].count("A")
        if knights[i] == "b":
            s += knights[i - 1000 : i + 1001].count("B")
        if knights[i] == "c":
            s += knights[i - 1000 : i + 1001].count("C")

print(s)
