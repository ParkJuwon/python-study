# 문자열
## Q1
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]
print(yyyymmdd)
print(num)
## Q2
pin = "881120-1068234"
print(num[0])

# 리스트
## Q1
a = [1,2,3,4,5]
a.sort()
a.reverse()
print(a)
## Q2
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 튜플
## Q1
a = (1,2,3)
a = a + (4,)
print(a)

# 딕셔너리
## Q1
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

# 집합
## Q1
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 변수
## Q1
a = b = [1,2,3]
a[1] = 4
print(b)
