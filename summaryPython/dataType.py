# 정수형(Integer) : 정수를 다루는 자료형
# 코딩 테스트에서 출제되는 많은 문제들은 정수형을 주로 다루게 된다.

# 양의 정수
a = 1000
print(a)

# 음의 정수
a = -7
print(a)

# 0
a = 0
print(a)

import sys
print(sys.version)

# 값 증가
a = a + 5
print(a)

# 실수형 : 소수점 아래의 데이터를 포함하는 수 자료형
# 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리됨
# 소수부가 0이거나, 정수부가 0인 소수는 0을 생략하고 작성할 수 있다.

# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 지수 표현 방식
# 파이썬에서는 e나 E를 이용한 지수 표현 방식을 이용한다.
# e나 E 다음에 오는 10의 지수부를 의미한다.
# 유효숫자e^(지수) = 유효숫자 * 10^(지수)
# ex. 1e9 = 10의 9제곱(10억)
# 지수 표현 형태는 실수형으로 처리됨
# 최단 경로 알고리즘에서 도달할 수 없는 노드에 대하여 최단 거리를 무한(INF)로 설정하곤 한다.
# 이때 가능한 최대값이 10억 미만이라면 무한(INF)의 값으로 1e9를 이용 가능.

# 1,000,000,000의 지수 표현 방식
a = 1e9
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3