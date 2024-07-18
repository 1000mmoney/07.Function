#  구구단 출력하라
for x in range(2, 10):
    print("\n", "[" + str(x) + "단]")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
