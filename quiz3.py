# # 8. 문자메시지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오. 메세지의 길이가 20이하이면
# # 50원이며, 20을 초과하면 100원이다. 사용자로부터 문자메시지를 입력 받아서 문자 요금을 반환하는
# # 코드를 작성하시오
#
# def massage(a):
#     b = len(a)
#     if 20 > b:
#         x = b * 100
#         print(x, "원입니다.")
#     elif 20 <= b:
#         y = b * 50
#         print(y, "원입니다.")
#     return x
#     return y
#
# a = input("문자메세지를 입력하세요:")
# massage(a)
#
# # 교수님

# 4. 문자 메시지를 입력받는다.
# x = input("문자메시지를 입력해주세요 : ")
# # 1. 문자 메시지의 길이를 파악
# x = "내가 입력하는 문자 메시지의 길이를 늘리겠습니다."
# print(len(x))
# 2. 문자 메시지의 길이 < 20, 50원

# 5. 함수로 만들어서 요금을 반환
def find_len(x):
    #  요금을 반환하기 위해서 변수 설정(초기화)
    result = 0
    if len(x) <= 20:
        print("50원")
        result = 50
    # 3. 문자 메시지의 길이 > 20, 100원
    elif len(x) > 20:
        result = 100
    return result

x = input("문자 메시지를 입력하세요 : ")
var = find_len(x)
print(var)
