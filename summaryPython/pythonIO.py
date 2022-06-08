# 기본 입출력
# 모든 프로그램은 적절한 (약속된) 입출력 양식을 가지고 있다.
# 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것.

# 자주 사용되는 표준 입력 방법
# input() 함수는 한 줄의 문자열을 입력 받는 함수이다.
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용한다.
# 예시) 공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용한다.
#   list(map(int, input().split()))
# 예시) 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용한다.
#   a, b, c = map(int, input().split())

# # 데이터의 개수 입력
# n = int(input())
# # 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# a, b, c를 공백을 기준으로 구분하여 입력
a, b, c = map(int, input().split())
print(a, b, c)