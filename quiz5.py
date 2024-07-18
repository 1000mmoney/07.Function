# my_list = [100, 200, 400, 800, 1000, 1300]
# result = 0
# def togher():
#
#     for i in my_list:
#         result = result + i
#     avg = result / len(my_list)
#     print(avg)
#
# var = int(input("점수를 입력하세요:"))
# a = score(var)
# print(a)
#

# v = int(input("리스트에 추가할 숫자를 입력하세요:"))
# v = []
# v.append(v)
#
# def togher(v):
#     result = 0
#     for i in v:
#         result = result + i
#     avg = result / len(v)
#     return result
#     print(avg)
#
# togher(20)



# 나
# def togher(x):
#     result = 0
#     for i in x:
#         result = result + i
#     avg = result / len(x)
#     print(avg)
#
#
# togher([20, 50])

# 교수님
def mean_list(var):
    result = 0
    for i in var:
        result = result + i
        avg = result / len(var)
        return avg

var = list(range(1, 300))
print(mean_list(var))