# # numbers = [100, 200, 300]
#
# n = [100, 200, 300]
# def sale(n):
#     result = []
#     for b in n:
#         result = b*0.1 + b
#     return result
#     print(VAT())
#
#
# sale(n)


# numbers_1 = []
# numbers_2 = []
# numbers_3 = []
#
# for i in range(1, 101):
#     if i % 2 == 0:
#        numbers_1.append(i)
#
#     if i % 3 == 0:
#         numbers_2.append(i)
#
#     if i % 5 == 0:
#         numbers_3.append(i)
#
#
# print(numbers_1)
# print(numbers_2)
# print(numbers_3)
#

# n = [100, 200, 300]
# for b in n:
#     print(b*0.1 + b)



# n = [100, 200, 300]
# def vat(n):
#     result = []
#     for b in n:
#         result = b*0.1 + b
#     return result
#
#  c = vat(n)
#  print(c)

# 교수님


def VAT(var):
    result_list = []
    for i in var:
        result_list.append(int(i*1.1))
    return result_list

x = [200, 300, 500]
print(VAT(x))