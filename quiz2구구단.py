# 7. 구구단 함수를 작성하시오. 매개변수 입력에 따라 해당 구구단을 화면에 출력하는 함수를 작성하시오.

# def mul(x):
#     for x in range(2, 10):
#         print("\n", "[" + str(x) + "단]")
#         for y in range(1, 10):
#             print(x, "X", y, "=", x * y)
#
# mul(2)


# 교수님

def print_mul_table(x):
    print("[", str(x), "단 ""]")
    for i in range(1, 10):
        print(x, "X", i, "=", x*i)

print_mul_table(6)