# 집합 자료형
# 특징 : 중복 허용 X, 순서가 없음
# 집합은 리스트 혹은 문자열을 이용해서 초기화 가능.
#  - set() 함수 이용.
# 혹은 중괄호({})안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화 할 수 있다.
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data) # 중복 원소는 제거됨

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산 : 수학과 동일
# 합집합, 교집합, 차집합

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

## 사전 자료형과 집합 자료형의 특징
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만
# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
# 사전의 키(key) 혹은 집합의 원소(element)를 이용해 O(1)의 시간 복잡도로 조회한다.
# 키나 원소의 값으로는 변경 불가능한 문자열이나 튜플과 같은 객체가 사용되어야 한다.