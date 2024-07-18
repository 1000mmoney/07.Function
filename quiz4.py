# 학점 변환기 함수. 점수 구간에 해당하는 학점이 아래와 같이 정의
# 사용자로부터 스코어를 입력 받ㅇ ㅏ학점으로 환산하여 바환하는 함수를 작성하여라
# 81~100 = A
# 61~80 = B
# 41~60 = C
# 21~40 = D
# 0~20 = E

def score(a):
    if 81 <= a <= 100:
        print("A")
    elif 61 <= a <= 80:
        print("B")
    elif 41 <= a <= 60:
        print("C")
    elif 21 <= a <= 40:
        print("D")
    else:
        print("E")

a = int(input("점수를 입력하세요:"))
score(a)

# 교수님

def score(var):
    result = ""
    if 81 <= var <= 100:
        result = "A"
    elif 61 <= var <= 80:
        result = "B"
    elif 41 <= var <= 60:
        result = "C"
    elif 21 <= var <= 40:
        result = "D"
    else:
        result = "E"
    return result

var = int(input("점수를 입력하세요:"))
a = score(var)
print(a)