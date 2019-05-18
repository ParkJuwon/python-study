# 복소수
a = 1 + 2j
b = 3-4J

print(a.real) # 실수
print(a.imag) # 허수
print(a.conjugate()) # 컬레복소수
print(abs(a)) # 절대값

print(7 / 4)
print(7 // 4) # 소수점 아랫자리 버림

a = "python"
print(a * 2) # 문자열 2번 나옴

# 인덱싱 슬라이싱
a = "Life is too short, You need Python"
print(a[-0])
print(a[-1])
print(a[0:4]) # [시작번호:끝번호]
print(a[19:]) # You need Python
print(a[:17]) # Life is too short
print(a[19:-7]) # You need

# 문자열 포매팅
print("i eat %d apples" % 3)
print("i eat %s apples" % "five")
number = 10
day = "three"
print("i ate %d apples. so I was sick for %s days." % (number, day))

print("Error is %d%%" % 98) # Error is 98%

# 문자열 관련 함수
a = "hobby"
print(a.count("b"))

a = "Python is best choice"
print(a.find('b'))
print(a.find('k'))

print(a.index('b'))
# print(a.index('k')) # 값이 없으므로 error 발생

# 문자열 삽입
a = ","
print(a.join('abcd'))

a = "hi"
print(a.upper())
a = "HI"
print(a.lower())
a = " hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I eat {0} apples {1}".format(3, 4))

print("I eat {name} apples {value}".format(name="3", value=4))


# 정렬
print("{0:<10}".format("hi")) # 왼쪽
print("{0:>10}".format("hi")) # 오른쪽
print("{0:^10}".format("hi")) # 가운데

# 공백 채우기
print("{0:=^10}".format("hi")) # ====hi====
print("{0:!<10}".format("hi")) # hi!!!!!!!!


# 소수점 표현
y = 3.421342132
print("{0:0.4f}".format(y)) # 3.4213
print("{0:10.4f}".format(y)) # 3.4213

print("{{and}}".format()) # {and}

# 리스트 슬라이싱
a = [1,2,3,4,5]
print(a[0:2])


# 리스트 더하기
a = [1,2,3]
b = [4,5,6]
print(a + b) # [1, 2, 3, 4, 5, 6]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(str(a[2]) + "hi")
print(a)
a[1:2] = ['a','b','c'] # 리스트를 리스트로 바꾼다
print(a) # [1, 'a', 'b', 'c', 3]

a = [1,2,3]
a[1] = ['a','b','c'] # 요소를 리스트로 바꾼다
print(a) # [1, ['a', 'b', 'c'], 3]

a = [1, 'a', 'b', 'c', 3]
a[1:3] = []
print(a) # [1, 'c', 3]
del a[1]
print(a) # [1, 3]

# 리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)

# 튜플
t1 = ()
t2 = (1,) # 단지 1개의 요소만 가질때 콤마를 반드시 붙혀야함
t4 = 1,2,3 # 괄호를 안써 됨


# 딕셔너리 추가
a = {1:'a'}
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}

# 삭제
del a[1]
print(a) # {2: 'b'}

# key 리스트 만들기
a = {'name' : 'john', 'phone' : '11111111111123', 'birth' : '1118'}
print(a.keys())
print(list(a.keys()))

for k in a.keys():
    print(k)

print(a.values()) # dict_values(['john', '11111111111123', '1118'])
print(a.items()) # dict_items([('name', 'john'), ('phone', '11111111111123'), ('birth', '1118')])

print(a.get('name'))
print(a.get('nokey')) # None
print(a.get('foo', 'bar')) # default value : bar

print('name' in a) # True
print('email' in a) # False

s1 = set([1,2,3])
print(s1) # {1, 2, 3}
s2 = set("Hello")
print(s2) # {'l', 'o', 'e', 'H'}

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2) # 교집합
print(s1.intersection(s2)) # 교집합

print(s1 | s2) # 합집합
print(s1.union(s2)) # 합집합

print(s1 - s2) # 차집합
print(s2 - s1) # 차집합
print(s1.difference(s2)) # 차집합
print(s2.difference(s1)) # 차집합

# 값 추가
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 여러개 추가
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

# 값 제거
s1 = set([1,2,3])
s1.remove(2)
print(s1)

print(type(3))
a = 3
b = 3
print(a is b)

import sys
print(sys.getrefcount(3))
a = 3
print(sys.getrefcount(3))
b = 3
print(sys.getrefcount(3))
c = 3
print(sys.getrefcount(3))

# 메모리에 생성된 변수 제거
a = 3
b = 3
del(a)
del(b)
print(sys.getrefcount(3))


# 리스트 복사
a = [1,2,3]
b = a # 참조
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 4, 3]
print(b is a)

a = [1,2,3]
b = a[:] # a 리스트 전체를 복사하여 b에 대입
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 2, 3]

# copy 모듈 이용
from copy import copy
b = copy(a)
print(b is a)

