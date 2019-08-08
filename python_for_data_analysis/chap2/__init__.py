a = 5
print(isinstance(a, int))

a = 5
b = 4.5
print(isinstance(a, (int, float)))
print(isinstance(b, (int, float)))

a = 'foo'
print(getattr(a, 'split'))  # hasattr, setattr 도 있음 (리플렉션)

"""
덕 타이핑

객체의 자료형에는 관심이 없고 그 객체가 어떤 메서드나 행동을 지원하는지만 알고 싶은 경우를 덕 타이핑이라고 함

'만일 오리처럼 걷고 오리처럼 꽥꽥 운다면 그것은 오리다' 라는 의미로 지어진 이름
예를 들어 어떤 객체가 '이터레이터'를 구현했다면 순회가 가능한 객체인지 검증할 수 있다.
이는 대부분의 객체의 경우 __iter__ 라는 '매직 메서드'를 가지고 있는지 확인하면 된다.
"""
print()


def isiterable(obj):
	try:
		iter(obj)
		return True
	except TypeError:  # iterable 객체 아님
		return False


print(isiterable('a string'))
print(isiterable([1, 2, 3]))
print(isiterable(5))

x = [1, 2, 3]
if not isinstance(x, list) and isiterable(x):
	x = list(x)

print()
# is 사용
a = [1, 2, 3]
b = a
c = list(a)
print(a is b)
print(a is not c)
print(a == c)

print()
a = None
print(a is None)

print()
s = r'this\has\no\special\characters'  # r은 raw 를 뜻함
print(s)

print()
template = '{0:.2f} {1:s} are worth US${2:d}'
print(template.format(4.5560, 'Argentine Pesos', 1))

print()
bytes_val = b'this is bytes'  # b는 바이트 표현
print(bytes_val)
decoded = bytes_val.decode('utf8')
print(decoded)

print()
print(type(None))

print()
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.day)
print(dt.minute)
print(dt.date())
print(dt.time())
print(dt.strftime('%m/%d/%Y %H:%M'))
print(datetime.strptime('20091031', '%Y%m%d'))
print(dt.replace(minute=0, second=0))
dt2 = datetime(2011,11,15,22,30)
delta = dt2 - dt
print(delta)
print(type(delta))
print(dt + delta)

"""
Datetime 포맷 규칙
%Y 4자리 연도
%y 2자리 연도
%m 2자리 월[01, 12]
%d 2자리 일[01, 31]
%H 시간(24시간 형식)[00, 23]
%I 시간(12시간 형식)[01, 12]
%M 2자리 분[00, 59]
%S 초[00, 61] (60, 61은 윤초)
%w 정수로 나타낸 요일[0(일요일), 6]
%U 연중 주차[00, 53] 일요일을 그 주의 첫 번째 날로 간주, 그 해에서 첫 번째 일요일 앞에 있는 날은 0주차
%W 연중 주차[00, 53] 월요일을 그 주의 첫 번째 날로 간주, 그 해에서 첫 번째 월요일 앞에 있는 날은 0주차
%z UTC 시간때 오프셋을 +HHMM 또는 -HHMM 으로 표현. 만약 시간대를 신경 쓰지 않는다면 비워둠
%F %Y-%m-%d 형식에 대한 축약(예: 2012-04-18)
%D %m/%d/%y 형식에 대한 축약(예: 04/18/12)
"""
print(dt.strftime('%F'))

