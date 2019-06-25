# 입력값이 몇개가 될지 모를때
def sum_many(*args):
	sum = 0
	for i in args:
		sum = sum + i
	return sum


print(sum_many(1, 2, 3, 4, 5, 6))


# tuple 리턴
def sum_and_mul(a, b):
	return a + b, a * b


result = sum_and_mul(3, 4)
sum, mul = sum_and_mul(3, 4)


# 초기값 설정
def say_myself(name, old, man=True):
	print("나의 이름은 %s 입니다." % name)
	print("나의 나이는 %d 입니다." % old)
	if man:
		print("남자")
	else:
		print("여자")


say_myself("1", 33)
say_myself("2", 33, False)
say_myself("2", 33, man=False)

# 외부 변수의 값을 적용하기 위해 global 명령사용
a = 1


def vartest():
	global a
	a = a + 1


vartest()
print(a)

print("life" "is" "too short")  # lifeistoo short
print("life" + "is" + "too short")  # lifeistoo short
print("life", "is", "too short")  # life is too short

# 한줄에 결과값 출력
for i in range(10):
	print(i, end=' ')

print()

# 파일 읽고 쓰기
# 쓰기 모드로 사용시 파일 존재하면 내용 지우고, 존재하지 않으면 파일 생성
f = open("새파일.txt", 'w')
f.close()  # 생략 가능 (파이썬 종료시 자동으로 닫아줌)

f = open("새파일.txt", 'w')
for i in range(1, 11):
	data = "%d번째 줄 입니다\n" % i
	f.write(data)
f.close()

f = open("잔나비_가사", 'r')
line = f.readline()
print(line)
f.close()

f = open("잔나비_가사")
while True:
	line = f.readline()  # readline() 은 더 이상 읽을 파일이 없을 경우 None 출력
	if not line: break
	print(line)
f.close()

f = open("잔나비_가사")
lines = f.readlines()  # 요소의 줄을 가지는 리스트 반환
for line in lines:
	print(line)
f.close()

f = open("잔나비_가사")
data = f.read()  # 파일 전체 내용을 문자열로 리턴
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open("새파일.txt", 'a')
for i in range(11, 20):
	data = "%d번째 줄입니다.\n" % i
	f.write(data)
f.close()

f = open("foo.txt", 'w')
f.write("Life is too short. you need python")
f.close()
### 파일을 열고 닫는것을 자동으로 처리하고 싶으 ㄹ때
with open("foo.txt", "w") as f:
	f.write("Life is too short. you need python")

