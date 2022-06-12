# 조건문
# 조건문은 프로그램의 흐름을 제어하는 문법이다.
# 조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있다.

from re import I


x = 15
if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x = 30")

# 들여쓰기
# 파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정한다.
# 다음의 코드에서 마지막 라인은 무조건 실행됩니다.

score = 85

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')
else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요')

print('프로그램을 종료합니다.')

# 탭을 사용하는 쪽과 공백 문자(space)를 여러 번 사용하는 쪽으로 두 진영이 있습니다.
# 이에 대한 논쟁은 지금까지도 활발하다.
# 파이썬 스타일 가이드라인에서는 4개의 공백 문자를 사용하는 것을 표준으로 설정하고 있다.

# 조건문의 기본 형태
# 조건문의 기본적인 형태는 if ~ elif ~ else
# 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 됨.

a = 5

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("-10 >= a")

# 비교 연산자
# 비교 연산자는 특정한 두 값을 비교할 때 이용가능.
# 대입 연산자(=)와 같음 연산자(==)의 차이점에 유의.

# 논리 연산자
# 논리 연산자는 논리 값(True/False) 사이의 연산을 수행할 때 사용한다.
# X and Y : 모두 참이어야 참
# X or Y : 하나만 참이면 참
# not X : X가 거짓일 때 참

# 파이썬의 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공된다.
# 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능하다.
# X in 리스트 : 리스트 안에 X가 들어가 있을 때 참이다.
# X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 참이다.

# 파이썬의 pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용한다.
# 예시) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우
score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

# 조건문의 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있다.

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

# 조건부 표현식(Conditional Expression)은 if ~ else문을 한 줄에 작성할 수 있도록 해줍니다.

score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# 파이썬 조건문 내에서의 부등식
# 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.
# 예를 들어 x > 0 and x < 20과 0 < x < 20은 같은 결과를 반환한다.

# 코드 스타일 1
x = 15
if x > 0 and x < 20:
    print('x는 0 이상 20 미만의 수입니다.')

# 코드 스타일 2
x = 15
if 0 < x < 20:
    print('x는 0 이상 20 미만의 수입니다.')

# 본 책에서는 다른 언어를 다룰 때 헷갈리지 않도록 x > 0 and x < 20와 같이 비교 연산자 사이에
# and, or 등의 연산자가 들어가는 형태의 코드를 이용한다.

# 반복문
# 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법이다.
# 파이썬에서는 while문과 for문이 있는데, 어떤 것을 사용해도 상관 없다.
# 다만 코딩 테스트에서의 실제 사용 예시를 확인해 보면, for문이 더 간결한 경우가 많다.

# 1부터 9까지 모든 정수의 합 구하기 예제(while문)
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# 1부터 9까지 홀수의 합 구하기 예제(while문)
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

# 반복문에서의 무한 루프
# 무한 루프(Infinite Loop) : 끊임없이 반복되는 반복 구문을 의미합니다.
# 코딩 테스트에서 무한 루프를 구현할 일은 거의 없으니 유의.
# 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인.

# 반복문 For
# for문의 구조는 특정한 변수를 이용하여 'in' 뒤에 오는 데이터(리스트, 튜플 등)에
# 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문한다.
# for 변수 in 리스트:
#     실행할 소스코드
array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용한다.
# 이 때 range(시작 값, 끝 값 +1)형태로 사용.
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 된다.

result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i

print(result)

# 1부터 30까지 모든 정수의 합 구하기 예제(for문)
result = 0
for i in range(1, 31):
    result += i

print(result)

# continue : 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 사용.

# 1부터 9까지의 홀수의 합(continue)
result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

# break : 반복문을 즉시 탈출
# 1부터 5까지의 정수를 차례대로 출력
i = 1

while True:
    print("현재 i의 값 :", i)
    if i == 5:
        break
    i += 1

# 예제
# 1. 학생들의 합격 여부 판단 예제 : 점수가 80점이 넘으면 합격

score = [90, 85, 77, 65, 97]

for i in range(5):
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 2. 학생들의 합격 여부 판단 예제 : 특정 번호의 학생은 제외하기

score = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 3. 중첩 반복문 : 구구단 예제
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print() # 단 별 나누기 위한 것(별거아님)