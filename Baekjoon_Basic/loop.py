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
T = int(input())
i = 1
list = []
while(i <= T):
    a, b = map(int, input().split())
    list.append(a+b)
    i += 1
for x in list:
    print(x)