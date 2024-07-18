# a = int(input("숫자를 입력하세요:"))
# b = a % 2
# if b == 0:
#     print("짝수입니다.")
# elif b == 1:
#     print("홀수입니다.")



# def frog(x):
#     result = ""
#     if x % 2 == 0:
#         result = "짝수입니다."
#     else:
#         result = "홀수입니다."
#     return result
#
# a = int(input("숫자를 입력하세요:"))
# b = frog(a)
# print(b)

# 교수님
var = 1233

def find_odd__even(var):
    result = ""
    if var % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result

res = find_odd_even(12345678)
print(res)