class Service:
	secret = "영구는 배꼽이 두 개다"
	def __init__(self, name):
		self.name = name
	def setname(self, name):
		self.name = name
	def sum(self, a,b):
		result = a + b
		print("%s님 %s + %s = %s 입니다." % (self.name, a, b, result))


pey = Service("홍길동")
pey.sum(1,1)

# babo = Service()
# babo.sum(1,1)

'''
클래스 구조

class 클래스이름[(상속클래스명)]:
	<클래스 변수 1>
	<클래스 변수 2>
	...
	<클래스 변수 N>
	
	def 클래스 함수1(self[,인수1,인수2,...]):
		<수행할 문장 1>
		<수행할 문장 2>
		...
		
	def 클래스 함수2(self[,인수1,인수2,...]):
		<수행할 문장 1>
		<수행할 문장 2>
		...
		
	def 클래스 함수N(self[,인수1,인수2,...]):
		<수행할 문장 1>
		<수행할 문장 2>
		...
'''

class FourCal():
	def setData(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		result = self.first + self.second
		return result

	def mul(self):
		result = self.first * self.second
		return result

	def sub(self):
		result = self.first - self.second
		return result

	def div(self):
		result = self.first / self.second
		return result


a = FourCal()
a.setData(1, 3)
b = FourCal()
b.setData(4, 2)

print("%d, %d, %d, %d" % (a.sum(), a.mul(), a.div(), a.sub()))
print("%d, %d, %d, %d" % (b.sum(), b.mul(), b.div(), b.sub()))

class HousePark:
	lastname = "박"

	def __init__(self, name):
		self.fullname = self.lastname + name
	def setname(self, name):
		self.fullname = self.lastname + name
	def travel(self, where):
		print("%s, %s여행을 가다." % (self.fullname, where))

	def love(self, other):
		print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))

	def fight(self, other):
		print("%s, %s 사랑에 싸우네" % (self.fullname, other.fullname))

	# 오버로딩
	def __add__(self, other):
		print("%s, %s 결혼했네" % (self.fullname, other.fullname))

	# 오버로딩
	def __sub__(self, other):
		print("%s, %s 이혼했네" % (self.fullname, other.fullname))

pey = HousePark("응용")
pey.travel("태국")

# 클래스의 상속
class HouseKim(HousePark):
	lastname = "김"

	#오버라이딩
	def travel(self, where, day):
		print("%s, %s여행 %d일 가네." % (self.fullname, where, day))

juliet = HouseKim("줄리엣")
juliet.travel("독도", 3)

pey.love(juliet)
pey + juliet
pey - juliet

import mod1
print(mod1.safe_sum(3, 4))
print(mod1.safe_sum(3, 'a'))


from mod1 import sum, safe_sum
# from mod1 import *
print(sum(3,4))
print(safe_sum(3,'a'))


import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.PI, 4.4))

'''
except [발생오류 [as 오류 메시지 변수]]:

1. try, except 만 쓰는경우
try:
	...
except:
	...
	
2. 발생 오류만 포함한 except 문
try:
	...
except 발생오류:
	...
	
3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
	...
except 발생오류 as 오류 메시지 변수:
	...

'''

try:
	4 / 0
except ZeroDivisionError as e:
	print(e)


'''
try .. else 
else 절은 예외가 발생하지 않은 경우에 실행, except 절 바로 다음 위치
'''
try:
	f = open("foo.txt", "r")
except FileNotFoundError as e:
	print(str(e))
else:
	data = f.read()
	f.close()


'''
try .. finally
try 문 수행도중 예외 발생여부와 상관없이 항상 수행
'''


try:
	f = open("없는 파일", "r")
except FileNotFoundError:
	pass ## 오류 회피


# 오류 일부러 발생시키기
class Bird:
	def fly(self):
		raise NotImplementedError # raise 키워드로 오류 발생, Bird 클래스를 상속받는 자식 클래스는 반드시 fly를 구현해야함

class Eagle2(Bird):
	def fly(self):
		print("very fase")

eagle = Eagle2()
eagle.fly()

'''
NotImplementedError 발생

class Eagle(Bird):
	pass

eagle = Eagle()
eagle.fly()
'''

########## 내장 함수
# 내장함수는 import 를 필요로 하지 않는다.

# abs: 절대값
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all: 반복 가능한 자료형이 모두 참이면 True
print(all([1,2,3])) # True
print(all([1,2,3,0])) # False

# any: 하나로 참이 있으면 True 모두 거짓일때 False
print(any([1,2,3,0])) # True
print(any([0, ""])) # False

# chr: ascii 코드값을 받아 코드에 해당하는 문자 출력
print(chr(97))
print(chr(48))

# dir: 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌, 리스트와 딕셔너리 객체의 관련 함수들을 보여주는 예
print(dir([1,2,3]))
print(dir({'1':'a'}))

# divmod: param1 를 param2로 나눈 몫과 나머지를 튜플로 리턴
print(divmod(7,3))
print(divmod(1.3,0.2))

# enumerate: 인덱스 값을 포함하는 객체 리턴
for i, name in enumerate(['body', 'foo', 'bar']):
	print(i, name)

# eval: 실행 가능한 문자열을 받아 실행한 결과값을 리턴 ( 문자열을 동적으로 실행할때 사용 )
print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))

# filter

# def positive(numberList):
# 	result = []
# 	for num in numberList:
# 		if num > 0:
# 			result.append(num)
# 	return result
# print(positive([1,-3,2,0,-5,6]))

def positive(x):
	return x > 0

print(list(filter(positive, [1,-3,2,0,-5,6])))
print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6])))

# hex: 16진수로
print(hex(234))
print(hex(3))

# id: 고유 주소값 리턴
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))

# input: 사용자 입력을 받음
# a = input()
# print(a)
# b = input("Enter: ")
# print(b)

# int(x, radix): 진수 표기
print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))

# isinstance
class Person: pass
a = Person()
print(isinstance(a, Person))

# lambda
sum = lambda a, b : a + b
print(sum(3,4))

myList  = [lambda a,b : a + b, lambda a,b : a * b]
print(myList[0](3,4))
print(myList[1](3,4))

# len
print(len("python"))
print(len([1,2,3]))

# list
print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3))) # [1, 2, 3]
a = [1,2,3]
b = list(a) # [1, 2, 3]

# map
def two_times(numberList):
	result = []
	for number in numberList:
		result.append(number * 2)
	return result

result = two_times([1,2,3,4])
print(result)

def two_times2(x): return x * 2
print(list(map(two_times2, [1,2,3,4])))

print(list(map(lambda a: a*2, [1,2,3,4])))

# max
print(max([1,2,3,4]))
print(max("python")) # y

# min
print(min([1,2,3,4]))
print(min("python")) # h

# oct: 8 진수로 변경
print(oct(34))
print(oct(12345))

# open(filename, [mode]): 파일 열기 기본은 r
# w, r, a(추가), b(바이너리)
# f = open("binary_file", "rb") # rb 는 바이너리 읽기모드

# ord: 아스키 코드값 리턴 (chr과 반대)
print(ord('a'))
print(ord('0'))

# pow(x, y): x의y 제곱 결과
print(pow(2,4))

# range
print(list(range(5))) # [0, 1, 2, 3, 4]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]
print(list(range(1, 10, 2))) # [1, 3, 5, 7, 9]

# sorted
print(sorted([3,1,2]))
print(sorted(['a', 'c', 'b']))

a = [3, 1, 2]
result = a.sort()
print(result) # None, 리턴값이 없음
print(a) # [1,2,3]

# str: 문자열로 변경
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

# tuple
print(tuple("abc")) # ('a', 'b', 'c')
print(tuple([1,2,3]))
print(tuple((1,2,3)))

# type : 자료형 확인
print(type("abc"))
print(type("abc"))
print(type(open("test","w")))

# zip: 동일한 개수로 이루어진 자료형을 묶어줌
print(list(zip([1,2,3], [4,5,6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1,2,3], [4,5,6], [7,8,9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc", "def"))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]


###### 외장 함수

# sys.argv: 인수 전달
import sys
print(sys.argv)

# sys.exit: 스크립트 강제 종료
# sys.path: 모듈들이 저장되어 있는 위치 나타냄
print(sys.path)
sys.path.append("/Users/user/develop/python-study/test")

# pickle: 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올수 있게 하는 모듈
import pickle
f = open("test.txt", "wb")
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

rb = open("test.txt", "rb")
data2 = pickle.load(rb)
print(data2)

# os module
# 환경 변수나 디렉터리, 파일등 os 자원 제어
import os
print(os.environ) # 리턴 객체가 딕셔너리
print(os.environ['PATH'])

# os.chdir: 현재 디렉터리 위치 변경
os.chdir("/Users/user")
print(os.getcwd())

# os.system(): 시스템 명령 호출
os.system("ls -al")

# os.popen(): 시스템 명령어를 실행시킨 결과값 받기
f = os.popen("ls -al")
print(f.read())

'''
os.mkdir: 디렉터리 생성
os.rmdir: 디렉터리 삭제 (파일들이 없어야함)
os.unlink: 파일을 삭제
os.rename(src, dst): src->dst rename
'''

# shutil: 파일 복사 모듈
import shutil
# shutil.copy("src.txt", "dst.txt")

# glob: 파일을 읽고 쓰는 기능에 대해 해당하는 모듈
# glob.glob(pathname): 파일들을 읽어서 리턴, *,? 등 가능
import glob
print(glob.glob("/Users/user/develop/python-study/jump_to_python/c*"))

# tempfile
import tempfile
filename = tempfile.mkdtemp()
print(filename)

f = tempfile.TemporaryFile() # 임시 저장공간으로 사용될 파일 객체 리턴, 기본적으로 바이너리 쓰기모드(wb)
f.close() # 객체는 자동으로 사라짐

# time
# time.time: UTC 를 이용, 현재시간 실수로 리턴
import time
print(time.time())

print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime()) # 현재시간만 return

print(time.strftime("%x", time.localtime(time.time()))) # 07/05/19
print(time.strftime("%c", time.localtime(time.time()))) # Fri Jul  5 17:24:25 2019
print(time.strftime("%Y-%m-%d %H:%M:%S.%s", time.localtime(time.time())))

# time.slepp
for i in range(10):
	print(i)
	# time.sleep(1) # 초

# calendar
import calendar
print(calendar.calendar(2015))
calendar.prcal(2015)

calendar.prmonth(2015, 12)

print(calendar.weekday(2015,12,31)) # 3 // 0:월 ~ 6:일
print(calendar.monthrange(2015, 12))

# random
import random
print(random.random())
print(random.randint(1,10))



