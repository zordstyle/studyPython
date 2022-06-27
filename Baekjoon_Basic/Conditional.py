### 1330번 : 조건문 사용법
# 조건문
# a, b = map(int, input().split())
# if a > b:
#     print(">")
# elif a < b:
#     print("<")
# else:
#     print("==")

######################################

### 2884번 : 알람 시계
# 현재시간에서 45분 전 시각 출력, 입력 시간은 24시간 표현을 사용한다.
# 출력 예제
# 10 10 -> 9 25
# 0 30 -> 23 45
# 23 40 -> 22 55

# 숫자 출력 시 str()로 형변환 해야한다.

# a, b = map(int, input().split())
# if b >= 45:
#     b -= 45
#     print(str(a) + " " + str(b))
# else:
#     b += 15
#     if a == 0:
#         print("23 " + str(b))
#     else:
#         a -= 1
#         print(str(a) + " " + str(b))

### 2525번 : 오븐 시계
h, b = map(int, input().split())
c = int(input())
m = b + c
output = str(h) + " " + str(m)
if m < 60:
    print(output)
else:
    h += m / 60
    m = m % 60
    if h >= 24:
        h = h % 24
        print(output)
    else:
        print(output)
