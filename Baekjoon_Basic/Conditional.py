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
# h, b = map(int, input().split())
# c = int(input())
# m = b + c
# if m < 60:
#     print(str(h) + " " + str(m))
# else:
#     h += int(m / 60)
#     m = m % 60
#     if h >= 24:
#         h = h % 24
#         print(str(h) + " " + str(m))
#     else:
#         print(str(h) + " " + str(m))

### 2480번 : 주사위 세개
# N = input().split()
# print(N)
# print(N[0])
# print(N[1])
# print(N[2])
# print(N[3])

a, b, c = map(int, input().split())
result = 0
if a == b and b == c and c == a:
    result = 10000 + (a * 1000)
    print(str(result))
elif (a == b and b != c):
    result = 1000 + (a * 100)
    print(str(result))
elif (b == c and c != a):
    result = 1000 + (b * 100)
    print(str(result))
elif (a == c and a != b):
    result = 1000 + (c * 100)
    print(str(result))
else:
    list = [a, b, c]
    result = max(list) * 100
    print(str(result))

# 다른 풀이법 (출처 : https://rsh1994.tistory.com/15)
# 집합을 이용한 문제 풀이
# 집합은 특성상 원소에 중복이 없다
#  -> 리스트를 집합화 시킨다면, 중복되는 것은 다 없어질 것이다.
# 1. 리스트가 모두 다 같은 눈이 나오면, 집합화 시켰을 때 원소의 개수가 1개일 것이다.
# 2. 리스트에서 2개의 눈이 같을 때, 집합화 시키면 원소의 개수가 2개일 것이다.
# 3. 리스트에서 모두 다른 눈이 나올 때, 집합화 시키면 원소의 개수가 3개이다.(그대로)

temp=input().split(" ") # 값을 받아옴(문자열)
list=[]
for i in temp:
    list.append(int(i)) # 정수형으로 바꿔서 list라는 배열에 넣음
list.sort() # 리스트 정렬
list_s = set(list) # 리스트를 집합화 시켜주고 list_s에 넣어줌

if len(list_s)==1 : # 모두 같은눈이 나왔을 때
    print(10000+list[0]*100)
elif len(list_s)==3 : # 모두 다른눈이 나왔을 때
    print(list[-1]*100)
else : # 2개가 같은눈이 나왔을 때
    print(1000+list[1]*100)  # 총 3개의 원소 중 정렬을 했을 때 중간이 같은수