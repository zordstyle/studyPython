# # 반복문 사용법
# array = [1, 2, 3, 4, 5]

# for x in array:
#     print(x)

# # i는 1부터 9까지의 모든 값을 순회
# result = 0
# for i in range(1, 10):
#     result += i

# # i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
# i = 1
# result = 0
# while i <= 9:
#     result += i
#     i += 1

### 10950번 : A + B -3
# 입력받은 수 만큼 반복 : while에 i = 1 하고 조건에 i <= (입력받은 수)
# T = int(input())
# i = 1
# list = []
# while(i <= T):
#     a, b = map(int, input().split())
#     list.append(a+b)
#     i += 1
# for x in list:
#     print(x)

# ### 8393번 : n까지의 합 구하기
# # 다른 소스 코드
# print(sum(list(range(1, int(input())+1))))
# # 또는 n까지의 합 공식 : n * (n+1) / 2

### 15552번 : 빠른 A+B
# for문 문제를 풀 때는 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다.
# Python의 경우 input 대신 sys.stdin.readline 사용 가능.
# 대신 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가해야 한다.
# 참고 글 #
# rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지, 개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다.
# 즉, int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없습니다. 
# 참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.

# 예제
# import sys
# a, b = map(int, sys.stdin.readline().split())
# print(a)
# print(b)

# input = sys.stdin.readline
# x, y = map(int, input().split())
# print(x)
# print(y)

# import sys
# T = int(sys.stdin.readline().rstrip())
# a = 0
# list = []
# while(a < T):
#     p, q = map(int, sys.stdin.readline().split())
#     list.append(p+q)
#     a += 1

# for x in list:
#     print(x)

### 11021번 : A+B -7
# import sys
# input = sys.stdin.readline
# T = int(input())
# list = []
# while(T >= 1):
#     a, b = map(int, input().split())
#     list.append(a+b)
#     T -= 1
# a = 1
# for x in list:
#     print("Case #"+str(a)+": "+str(x))
#     a += 1

### 11022번 : A+B -8
# str()에러 : string은 integer로 바로 변환 불가
import sys
print = sys.stdin.readline

T = int(input())
for x in range(1, T+1):
    print(x)
    a, b = map(int, input().split())
    print(f'Case #{x}: {a} + {b} = {a+b}')