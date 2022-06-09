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

# 빠르게 입력받기
# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# 파이썬의 경우 sys 라이브러리에 정의된 sys.stdin.readline() method 사용
# 단 입력 후 엔터가 줄 바꿈 기호로 되므로 rstrip() method 함께 사용
# 시간/초 판정, 이진탐색, 정렬, 그래프 관련 문제에서 자주 사용되는 테크닉

import sys

# 문자열 입력 받기
# data = sys.stdin.readline().rstrip()
# print(data)

# 자주 사용되는 표준 출력 방법
# 파이썬에서 기본 출력은 print() 함수 사용
# 각 변수를 콤마를 이용하여 띄어쓰기로 구분하여 출력할 수 있다.
# print()는 기본적으로 출력 이후에 줄 바꿈을 수행한다.
# 줄 바꿈을 원하지 않는 경우 'end' 속성 이용

# 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=' ')

# 출력할 변수
answer = 7
print("정답은 "+str(answer)+"입니다.") # 정수형을 문자형으로 변환

# f-string 예제
# 파이썬 3.6부터 사용 가능, 문자열 앞에 접두사 f를 붙여 사용
# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.
answer = 7
print(f"정답은 {answer}입니다.")

# # 데이터의 개수 입력
# n = int(input())
# # 각 데이터를 공백을 기준으로 구분하여 입력
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# a, b, c를 공백을 기준으로 구분하여 입력
a, b, c = map(int, input().split())
print(a, b, c)
