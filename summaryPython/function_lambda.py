# 함수(function) : 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미
# 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있다.
# 함수의 종류
#  1) 내장 함수 : 파이썬이 기본적으로 제공하는 함수
#  2) 사용자 정의 함수 : 개발자가 직접 정의하여 사용하는 함수

# 함수 정의하기(def, define)
# 함수를 사용하면 소스코드의 길이를 줄일 수 있다.
#  1) 매개 변수 : 함수 내부에서 사용할 변수
#  2) 반환 값 : 함수에서 처리 된 결과를 반환

# def 함수명(매개변수(parameter)):
#     실행할 소스코드
#     return 반환 값
# 호출 방법 : 함수명(인자(argument))

# 더하기 함수 예시 1)
from re import A


def add(a, b):
    return a + b

print(add(3, 7))

# 더하기 함수 예시 2)
def add(a, b):
    print('함수의 결과 :', a + b)

add(3, 7)

# 파라미터 지정하기
# 파라미터의 변수를 직접 지정할 수 있다.
# 이 경우 매개변수의 순서가 달라도 상관 없다.
def add(a, b):
    print('함수의 결과 :', a + b)

add(b = 3, a = 7)

# global 키워드
# global 키워드로 변수 지정 시 해당 함수에서는 지역변수를 만들지 않고,
# 함수 바깥에 선언된 변수를 바로 참조하게 된다.

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 값을 변경하는 것이 아닌 대입 또는 그대로 출력 등이면 안써도 된다.

a = 20

def func2():
    print(a + 20)

func2()

# 전역 변수로 리스트가 선언되어 있을 때, 이 리스트 내부 메소드를
# 함수 내부에서 호출하는 것은 오류없이 잘 동작한다.

array = [1, 2, 3, 4, 5]

def func3():
    array.append(6)
    print(array)

func3()

# 전역 변수명과 지역 변수명이 동일하다면
# 함수 내부에서는 지역 변수가 우선적으로 적용된다.

array = [1, 2, 3, 4, 5]

def func4():
    array = [3, 4, 5]
    array.append(6)
    print(array)

func4() # 지역변수 우선
print(array) # 전역변수 우선

# 코테에서는 리스트 변수는 전역변수로 선언하는 경우가 많고 
# 함수에서도 바로 참조하도록 하는 경우가 많기 때문에 
# 전역 변수/지역 변수 스코프 설정이 크게 중요하진 않지만 알긴 해야함

# 여러 개의 반환 값
# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.
# C/C++ 에서는 포인터 또는 구조체를 사용하는 것이 보통이다.

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var # 패킹 : 묶여서 한꺼번에 반환

a, b, c, d = operator(7, 3) # 언패킹 : 반환된 값들을 특정 변수에 담는 것
print(a, b, c, d)

# 람다 표현식 : 함수를 간단하게 작성할 수 있다.
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징이다. (이름 없는 함수)

def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(13, 7))

# 람다 표현식이 좋은 경우 : 어떤 함수 자체를 입력으로 받는 또 다른 함수가 있는 경우, 함수의 기능이 간단하거나 한 번만 사용하는 경우, 