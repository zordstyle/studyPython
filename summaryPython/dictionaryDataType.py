# 사전 자료형은 키와 값의 쌍을 데이터로 가지는 자료형
#  - 앞에 다룬 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됨.
# 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 불가능한 자료형'을 키로 사용 가능.
# 파이썬의 사전 자료형은 해시 테이블(hash table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 사전 자료형 관련 method
# 키 데이터만 뽑아서 리스트로 이용할 때 : keys()
# 값 데이터만 뽑아서 리스트로 이용할 때 : values()

# 키 데이터만 담은 list
key_list = data.keys()

# 값 데이터만 담은 list (형변환)
value_list = list(data.values())

print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])