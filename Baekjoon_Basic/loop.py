# 반복문 사용법
array = [1, 2, 3, 4, 5]

for x in array:
    print(x)

# i는 1부터 9까지의 모든 값을 순회
result = 0
for i in range(1, 10):
    result += i

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
i = 1
result = 0
while i <= 9:
    result += i
    i += 1