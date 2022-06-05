# 리스트 자료형
# 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형이다.
# 사용자 입장에서 C나 자바에서의 배열(Array)의 기능 및 Linked List와 유사한 기능을 지원한다.
# C++의 STL vector와 기능적으로 유사하다.
# 리스트 대신에 배열 혹은 테이블이라고 부르기도 한다.
# append, delete 등 유용한 기능 지원
# 리스트 초기화 : 대괄호([])안에 원소를 넣고 쉼표(,)로 원소를 구분
# 리스트의 원소에 접근할 때는 인덱스(Index)값을 괄호에 넣는다(인덱스는 0부터 시작)

# 직접 데이터를 넣어 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

# 네 번째 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 특정 값 바꾸기
a[4] = 4
print(a)

# 리스트의 인덱싱과 슬라이싱
# 인덱싱 :  인덱스 값을 입력하여 리스트의 특정한 원소에 접근하는 것
# 파이썬의 인덱스 값은 양의 정수와 음의 정수를 모두 사용할 수 있다.
# 음의 정수를 넣으면 원소를 거꾸로 탐색하게 된다. (-1부터 차례대로 작아진다)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 여덟 번째 원소만 출력
print(a[7])

# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 뒤에서 세 번째 원소 출력
print(a[-3])

# 네 번째 원소 값 변경
a[3] = -7
print(a)

# 슬라이싱 : 리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때는 슬라이싱을 이용한다.
# 대괄호 안에 콜론(:)을 넣어서 시작 인덱스와 끝 인덱스를 설정할 수 있다.
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정한다.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 네 번째 원소만 출력
print(a[3])
 
# 두 번째 원소부터 네 번째 원소까지
print(a[1:4])

# List Comprehension : 리스트를 초기화 하는 방법 중 하나
# 대괄호 안에 조건문과 반복문을 적용하여 리스트를 초기화 할 수 있다.

# 0~9의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)

# 0~49
a = [i for i in range(50)]
print(a)

# 0~19의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i & 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# 코드1 : List Comprehension
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 코드2 : 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

## List Comprehension은 2차원 리스트를 초기화 할 때 효과적으로 사용될 수 있다.
# N * M 크기의 2차원 리스트를 한 번에 초기화 해야할 때 매우 유용하다. (문제 상황이 이래서 유용)
# ex. array = [[0] * m for _ in range(n)]
# 잘못된 예시 : array = [[0] * m] * n 
# (전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식됨, 참조값을 복사하는 것)

# N * M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

array[1][1] = 5
print(array) # [[0, 0, 0], [0, 5, 0], [0, 0, 0], [0, 0, 0]]

# N * M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 4
m = 3
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array) # [[0, 5, 0], [0, 5, 0], [0, 5, 0], [0, 5, 0]]

# 언더바(_)
# 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.
# 1. 1~9까지의 자연수 더하기
summary = 0
for i in range(1, 10):
    summary += i
print(summary)

# 2. hello world를 5번 출력하기
for _ in range(5):
    print('hello world')

# 자주 사용하는 리스트 관련 method
# append() : 리스트에 원소를 하나 삽입할 때 사용한다.
# 사용법 : 변수명.append() / 시간복잡도 : O(1)
# sort() : 기본 정렬 기능으로 오름차순으로 정렬한다.
# 사용법 : 변수명.sort() / 시간복잡도 : O(NlogN)
# sort(reverse = True) : 내림차순으로 정렬한다.
# 사용법 : 변수명.sort(reverse = True) / 시간복잡도 : O(NlogN)
# reverse() : 리스트의 원소의 순서를 모두 뒤집어 놓는다.
# 사용법 : 변수명.reverse() / 시간복잡도 : O(N)
# insert() : 특정한 인덱스 위치에 원소를 삽입할 때 사용한다.
# 사용법 : insert(삽입할 위치 인덱스, 값) / 시간복잡도 : O(N)
# count() : 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.
# 사용법 : 변수명.count(특정 값) / 시간복잡도 : O(N)
# remove() : 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다.
# 사용법 : 변수명.remove(특정 값) / 시간복잡도 : O(N)

# 리스트 관련 기타 method
a = [1, 4, 3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)

a = [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기 :", a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가 :", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제 :", a)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)