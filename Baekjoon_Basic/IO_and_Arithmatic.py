### 1000 번 : input 사용법 

# input() : 입력된 값 문자열로 인식
# 괄호 안에 문자열 넣으면 인터페이스로 활용
# N = input("당신의 이름은...?: ")

# 입력값을 숫자로 : int 함수 사용
# N = int(input("입력 : "))

# 한 줄에 입력값 두 개 이상 구분 : split() 함수 사용
# split() : 띄어 쓰기를 기준으로 한 문자열을 나누어 리스트로 구분해준다.
# a = "This is baekjoon's homepage"
# print(a.split()) # ['This', 'is', "baekjoon's", 'homepage']

# input()와 split()을 결합하면?
# N = input().split() # 입력값 : 11 12 13 14
# print(N) # 출력값 : ['11', '12', '13', '14']

# 입력값 두 개 이상으로 구분
# A, B = input().split() # 입력값 : 11, 12
# print(A) # 11
# print(B) # 12

# 두 수를 입력받아 합을 출력
# A, B = input().split()
# x = int(A)
# y = int(B)

# int() 함수는 리스트를 정수형으로 변경할 수 없다. 또한 int()는 하나의 값에만 적용 가능.
# A, B = int(input().split()) # 에러

# map() 함수
# 사용법 : map(적용할 함수, 반복 가능한 자료형)
# A, B = map(int, ['231', '23234'])
# print(A, B) # 231 23234

# 두 수를 입력 받아 합을 출력 (map 함수 사용)
a, b = map(int, input().split())
print(a+b)

############################################

### 10869번

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# 출력 조건 중 나누기(a/b)가 몫만 나와야 하기 때문에 int 추가해줘야 함.
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(int(a/b))
# print(a%b)

# 참고 - 새싹
# print('         ,r\'"7')
# print('r`-_   ,\'  ,/')
# print(' \\. ". L_r\'')
# print('   `~\\/')
# print('      |')
# print('      |')