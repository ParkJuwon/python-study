# 튜플
tup = 4, 5, 6
print(type(tup))
print(tup)
print()

nested_tup = (4, 5, 6), (7, 8)
print(type(nested_tup))
print(nested_tup)

values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a, b)
print(rest)
a, b, *_ = values
print()

a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))

print()
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b)

print('\n' * 2)
"""
bisect 모듈은 이진 탐색과 정렬된 리스트에 값을 추가하는 기능을 제공
bisect.bisect 메서드는 값이 추가될 때 리스트가 정렬된 상태를 유지할 수 있는 위치를 반환하며
bisect.insort 는 실제로 정된 상태를 유지한 채 값을 추가
"""
import bisect

c = [1, 2, 2, 2, 3, 4, 7]
print(bisect.bisect(c, 2))
print(bisect.bisect(c, 5))
bisect.insort(c, 6)
print(c)

print()
'''
리스트 슬라이싱 스텝
'''
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[::2])
print(seq[::-1])

print()
'''
아이템 색인 enumerate(collection)
zip 함수를 사용하여 짝지어진 순차 자료형을 다시 풀어낼 수 있다. 
'''
# 리스트의 로우를 리스트의 컬럼으로
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)
print(last_names)

print()
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
	letter = word[0]
	if letter not in by_letter:
		by_letter[letter] = [word]
	else:
		by_letter[letter].append(word)

print(by_letter)

by_letter2 = {}
for word in words:
	letter = word[0]
	by_letter2.setdefault(letter, []).append(word)

print(by_letter2)
print()

from collections import defaultdict

by_letter3 = defaultdict(list)
for word in words:
	by_letter3[word[0]].append(word)
print(by_letter3)

print()
'''
유효한 사전 키
hash가 되어야 함 (값이 바뀌지 않는 객체만 가능)
'''
print(hash('string'))
print(hash((1, 2, (2, 3))))
try:
	print(hash((1, 2, [3, 4])))
except:
	pass

'''
파이썬 집합 연산
a.add(x) : a 에 원소 b 추가
a.clear() : 모든 원소를 제거
a.remove(x) : a에서 원소 x 제거
a.pop() : 임의의 원소 제거 비어 있는 경우 KeyError 발생

a.union(b) : 합집합 ( a | b )
a.update(b) :  합집합을 대입한다 ( a |= b )
a.intersection(b) : 교집합 ( a & b )
a.intersection_update(b) : 교집합을 대입한다 ( a &= b )
a.difference(b) : 차집합 ( a - b )
a.difference_update(b) : 차집합을 대입한다 ( a -= b )
a.symmetric_difference(b) : 대칭차집합 ( a ^ b )
a.symmetric_difference_update(b) : 대칭차집합을 대입한다 ( a ^= b )

a.issubset(b) : a의 모든 원소가 b에 속할 경우 True
a.issuperset(b) : a 가 b의 모든 원소를 포함 True
a.isdisjoint(b) : a 와 b 모두 속하는 원소가 없을 경우 True
'''

'''
리스트 표기법
[expr for val in collection if condition]
'''

'''
사전 표기법
dict_comp = {key-expr : value-expr for value in collection
			if condition}
'''

'''
함수의 스코프 밖에서 변수의 값을 대입하려면 global 사용

a = None

def bind_a_variable():
	global a
	a = []

bind_a_variable()
print(a)

자주 사용은 하지 않도록 함. 시스템 전체의 상태를 저장하기 위한 용도로 사용
'''

'''
커링
'''
def add_numbers(x, y):
	return x + y

add_five = lambda y: add_numbers(5, y)
print(add_five)
# 과정 단순화
from functools import partial
add_five = partial(add_numbers, 5)
print(add_five)



