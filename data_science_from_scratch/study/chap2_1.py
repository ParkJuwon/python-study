# -*- coding: utf-8 -*-

from __future__ import division # 5/2 = 2.5가 되게 해주는 


for i in [1,2,3,4,5]:
    print i
    for j in [1,2,3,4,5]:
        print j
        print i + j
    print i
print "done looping"

two_plus_three = 2 + \
    3

import re
my_regex = re.compile("[0-9]", re.I)

import re as regex
my_regex = regex.compile("[0-9]", regex.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()


### wrong
match = 10
from re import *
print match
### wrong end

def double(x):
    """이곳은 함수에 대한 설명을 적어 놓는 공간이다.
    예를들어, "이함수는 입력된 변수에 2를 곱한 값을 출력해 준다" 
    라는 설명을 추가할 수 있다"""
    return x * 2

# 파이썬 함수들은 변수로 할당되거나 함수의 인자로 전달할 수 있다는 점에서 일급 함수 특성을 가진다
def apply_to_one(f):
    """인자가 1인 함수 f를 호출"""
    return f(1)

my_double = double
x = apply_to_one(my_double)

# 짧은 익명의 람다 함수도 간편하게 만들수 있다
y = apply_to_one(lambda x: x + 4)

# 변수에 람다함수 생성 가능
another_double = lambda x: 2 * x # 이방법은 최대한 피하도록
def another_double(x): return 2 * x #대신 이렇게 작성

# 함수 인자에 기본값 할당 가능
def my_print(message = "my default message"):
    print message

my_print("hello")
my_print()

# 가끔씩 인자의 이름을 명시해 주면 편리
def subtract(a=0, b=0):
    return a - b

subtract(10, 5)
subtract(0, 5)
subtract(b = 5)

# 문자열은 작은 따옴표 또는 큰따옴표로 묶어 나타낸다 
single_quoted_string = 'data science'
double_quoted_string = "data science"

# 특수 문자 인코딩할 때 역슬래시 사용
tab_string = "\t"
len(tab_string)

# 만약 역슬래시로 보이는 문자로 사용하고 싶다면 문자열 앞에 r (raw string : 가공되지 않은 문자열) 을 명시
not_tab_string = r"\t"
len(not_tab_string)

# 세개의 따옴표를 사용하여 하나의 문자열을 여러 줄로 나눠서 나타낼수 있음
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# 코드가 뭔가 잘못됐을 때 파이썬은 예외(Exception)가 발생했음을 알려준다.
# try:
#     print 0 / 0
# except ZeroDivisionError
#     print "cannot divide by zero"

# list 는 순서가 있는 자료의 집합(collection) 
integer_list = [1,2,3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)
list_sum = sum(integer_list)

# 대괄호를 사용해 list 의 n 번째 값을 불러오거나 설정할 수 있다.
x = range(10)
zero = x[0]
one = x[1]
nine = x[-1] # list 의 마지막 항목을 가장 파이썬 스럽게 불러오는 방법
eight = x[-2] # 뒤에서 두 번째 항목을 가장 파이썬 스럽게 불러오는 방법
x[0] = -1 # x는 이제 -1,1,2,3,4,....,9

# 대괄호를 사용해 list를 나눌 수도 있다
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

# 파이썬에서는 제공하는 in 연산자를 사용하면 list 안에서 항목의 존재 여부를 확인 가능
1 in [1,2,3]  # True
0 in [1,2,3]  # Flase
# in 존재 여부 검사는 list 의 항목을 하나씩 확인해 보기 때문에 list의 크기가 작을때만 사용

# list 연결
x = [1,2,3]
x.extend([4, 5, 6])

# x를 수정하고 싶지 않다면 list를 더해줄 수 있다.
x = [1,2,3]
y = x + [4,5,6]

# 주로 list에 항목을 하나씩 추가하는 경우가 많다.
x = [1,2,3]
x.append(0)
y = x[-1]
z = len(x)

# 만약 list 안에 몇 개의 항목이 존재하는지 알고 있다면 손쉽게 list를 풀 수도(unpack) 있다
x, y = [1, 2]

# 하지만 양쪽 항목의 개수가 다르다면 ValueError가 발생
# 보통 버릴 항목은 밑줄로 표시
_, y = [1,2]

# tuple은 변경할 수 없는 listdlek. list에서 수정을 제외한 모든 기능을 tuple에 적용할 수 있다. tuple은 대괄호 대신 괄호 사용
my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"

# 함수에서 여러 값을 반환할 때 tuple을 사용하면 편하다.
def sum_and_product(x, y):
    return (x+y),(x*y)
sp = sum_and_product(2,3)
s, p = sum_and_product(5, 10)

# tuple과 list는 다중 할당 (multiple assignment)을 지원한다
x, y = 1, 2
x, y = y, x # 가장 파이썬 스럽게 변수를 교환

# dictionary(사전) 는 파이썬의 또다른 기본적인 데이터 구조이며, 특정 value와 연관된 key를 연결해 주고 이를 사용해 value 를 빠르게 검색 할 수 있다.
empty_dict = {} # 가장 파이썬 스럽게 dict를 만드는 방법
empty_dict2 = dict() # 덜 파이썬 스럽게 dict를 만드는 방법
grades = {"Joel" : 80, "Tim" : 95}

# 대괄호를 사용해서 key의 value를 불러올 수 있다
joels_grade = grades["Joel"]

# 만약 dict 에 존재하지 않는 key를 입력하면 KeyError가 발생한다
try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"


# 연산자 in을 사용하면 key 존재 여부 확인
joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False

# dict 에서 get method를 사용하면 입력한 key가 dict에 없어도 에러를 반환하지 않고 기본값을 반환
joels_grade = grades.get("Joel", 0) # 결과는 80
kates_grade = grades.get("Kate", 0) # 결과는 0
no_ones_grade = grades.get("No One") # 기본값으로 None을 반환

# 또한 대괄호를 사용해서 key와 value를 새로 지정해 줄 수 있다.
grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

# 정형화된 데이터를 간단하게 나타낼 때는 주로 dict가 사용
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
# 특정 key 대신 dict의 모든 key 를 한번에 살펴볼 수 있다.
tweet_keys = tweet.keys() # key에 대한 list
tweet_values = tweet.values() # value에 대한 list
tweet_items = tweet.items() # (key, value) tuple에 대한 list

"user" in tweet_keys # True. 하지만 list에서 in을 사용하기 떄문에 느림
"user" in tweet # 훨씬 파이썬 스럽고 dict에서 in을 사용하기 때문에 빠름
"joelgrus" in tweet_values # True
# dict의 key는 수정할 수 없으면 list를 key로 사용할 수 없다. 
# 만약 다양한 값으로 구성된 key가 필요하다면 tuple이나 문자열을 key로 사용

# defaultdict
document = ["#data", "#science", "#datascience", "#awesome", "#yolo"]

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


# 용서를 구하는게 허락을 받는 것보다 쉽다(forgiveness is better than permission) 는 마음가짐으로 
# 예외를 처리하면서 dict를 생성하는 방법도 있다.
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# 존재하지 않는 key를 적절하게 처리해 주는 get을 사용해서 dict 를 생성
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# 세가지 방법이 모두 복잡함. defaultdict을 사용하면 편해짐
# defaultdict와 평범한 dict의 유일한 차이점은 만약 존재하지 않는 key가 주어진다면 defaultdict는 이 key와
# 인자에서 주어진 값으로 dict에 새로운 항목을 추가해 준다는 것이다.
# 사용을 위해 collections 모듈에서 defaultdict을 불러줌

from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

# list, dict 혹은 직접 만든 함수를 인자에 넣어줄 수 있다.
dd_list = defaultdict(list)
dd_list[2].append(1) 
dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1


# Counter는 연속된 값을 defaultdict(int) 와 유사한 객체로 변환해 주며, key와 value의 빈도를 연결시켜 준다.
# 앞으로 히스토그램을 그릴 때 자주 사용할 것이다.
from collections import Counter
c = Counter([0, 1, 2, 0])

# 게다가 특정 문서에서 단어의 개수를 셀 때도 유용
word_counts = Counter(document)

# Counter 객체에는 굉장히 유용하게 쓰이는 most_common 함수가 있다.
# 가장 자주 나오는 단어 10개와 이 단어들의 빈도수 출력
for word, count in word_counts.most_common(10):
    print word, count


# set은 파이썬의 데이터 구조 중 유일한 항목의 집합을 나타내는 구조
s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s
z = 3 in s
# in은 set에서 굉장히 빠르가 작동

# 다른 언어의 null 처럼 파이썬에서는 존재하지 않는 값을 None으로 표기한다.
x = None
print x == None # True가 출력 하지만 파이썬스럽지 않다.
print x is None # True가 출력 이제 파이썬 스럽다.

# 거짓을 의미하는 방법
# False, None , [] (빈 list), {} (빈 dict), "", set(), 0, 0.0

# 나머지 거의 모든 것은 참(True)을 의미함.
s = []
if s: 
    first_char = s[0]
else:
    first_char = ""
# 위 코드는 다음과 같이 더욱 간단하게 표현
first_char = s and s[0]
# and는 첫번째 값이 참이면 두번째 값을 반환해 주고, 첫번째 값이 거짓이면 첫번째 값을 반환해 준다.
safe_x = x or 0
# 만약 x가 숫자거나 None 이라면  safe_x는 항상 숫자일 것이다

# 파이썬에는 list의 모든 항목이 참이라면 True를 반환해 주는 all 함수와 
# 적어도 하나의 항목이 참이라면 True를 반환해 주는 any 함수가 있다.
all([True, 1, {3}])
all([True, 1, {}])
any([True, 1, {}])
all([]) # True, 거짓인 항목이 하나도 없기 때문에
any([]) # False, 참인 항목이 없기 때문에


# 파이썬의 list에는 list를 자동으로 정렬해 주는 sort 메서드가 있다. 
# 만약 이미 만든 list를 망치고 싶지 않다면 sorted 함수를 사용해서 새롭게 정렬된 list를 생성
x = [4,1,2,3]
y = sorted(x)
x.sort()
# 기본적으로 오름차순, 내림차수는 인자에 reverse = True 추가
# 그리고 리스트의 각 항목끼리 서로 비교하는 대신 key를 사용하면 지정한 함수의 결과값을 기준으로 list 정렬

x = sorted([-4, 1, -2, 3], key=abs, reverse= True)

# 빈도의 내림차순으로 단어와 빈도를 정렬
wc = sorted(word_counts.items(), key= lambda(word, count): count, reverse=True)


# 기존 list에서 특정 항목을 선택하거나 변환시킨 결과를 새로운 list에 저장해야 하는 경우도 자주 발생
# 가장 파이썬 스럽게 처리하는 방법은 list comprehension이다

even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]
squares = [x * x for x in range(5)] # [0, 1, 4, 9 ,16]
even_squares = [x * x for x in even_numbers]

# 또한 dict나 set으로 변환시킬 수 있다.
square_dict = {x : x * x for x in range(5)}
square_set = {x * x for x in [1, -1]}

# 보통 list에서 불필요한 값은 밑줄로 표기
zeros = [0 for _ in even_numbers]

# List comprehension에는 여러 for를 포함할 수 있다.
pairs = [(x, y) 
        for x in range(10)
        for y in range(10)]

# 뒤에 나오는 for는 앞에 나온 결과에 대해 반복한다
increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]

# Generator는 (주로 for 문을 통해서) 반복할수 있으며, generator의 각 항목은 필요한 순간에 그때그때 생성된다.
# Generator를 만드는 한가지 방법은 함수와 yield를 활용하는것
def lazy_range(n):
    """range와 똑같은 기능을 하는 generator"""
    i = 0 
    while i < n:
        yield i
        i += 1


for i in lazy_range(10):
    print i

# 실제로 파이썬에서는 xrange라는 이름으로 lazy_range 함수가 이미 구현되어 있다.
# 파이썬 3에서는 range 자체가 generator로 만들어졌다. 
# 이는 무한한 수열도 메모리의 제약을 받지 않고 구현할 수 있다는 것을 의미한다.

def natural_numbers():
    """1,2,3, ... 을 반환"""
    n = 1
    while True:
        yield n
        n += 1

# break 없이 무한 수열을 생성하는 것은 추천하지 않는다.
# Generator의 단점은 generator를 단 한번만 반복할 수 있다는 점.
# 데이터를 여러번 반복해야 한다면 매번 generator를 다시 만들거나 list를 사용

# 또한 괄호 안에 for문을 추가하는 방법으로도 generator를 만들수 있다.
lazy_evens_below_20 = (i for i in lazy_range(20) if  i % 2 == 0)

# 나중에 dict 에서 generator로 key, value를 한번씩만 살펴보는 iteritems() 메서드를 자주 사용


# 난수 생성 = random 모듈 사용
import random
four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms


# 동일한 난수를 계속 사용하고 싶다면 random.seed 사용
random.seed(10)
print random.random()
print random.random()
random.seed(10)
print random.random()


# 인자가 1개 혹은 2개인 random.randrage를 사용하면 range() 에 해당 하는 구간 난수 생성 가능
random.randrange(10)
random.randrange(3,6)

# random shuffle 은 list의 항목의 임의 순서로 재정렬해 준다.
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

# random.choice 메서드를 사용하면 list의 임의의 항목을 하나 선택할 수 있다
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])

# random.sample 을 사용하면 list에서 중복이 허용되지 않는 임의의 표본 list를 만들수 있다
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print winning_numbers

# 중복이 허용되는 임의의 표본 list를 만들고 싶다면 random.choice 메서드를 여러번 사용하면 된다.
four_with_replacement = [random.choice(range(10)) 
                        for _ in range(4)]
print four_with_replacement

# 정규 표현식 사용
import re
print all([ # 모두 True
    not re.match("a", "cat"),  # 'cat'은 a로 시작하지 않기 때문에
    re.search("a", "cat"), # 'cat' 안에는 'a'가 존재하기 때문에
    not re.search("c", "dog"), # 'dog' 안에는 'c'가 존재하지 않기 때문에
    3 == len(re.split("[ab]", "carbs")), # a혹은 b 기준으로 나누면 ['c', 'r', 's']가 생성

    "R-D-" == re.sub("[0-9]", "-", "R2D2") # 숫자를 "-"로 대체 
]) # True가 출력됨

# 클래스의 이름은 관습에 따라 파스칼케이스로 표기
class TestSet:
    # 이제 맴버 함수들을 정의
    # 모든 맴버 함수의 첫번째 인자는 "self" 이다 (관습중 하나)
    # "self" 란 현재 사용되고 있는 Set 객체를 의미

    def __init__(self, values=None):
        """이것은 constructor(생성자) 이다
        새로운 Set을 만들면 호출된다
        다음과 같이 사용 가능
        s1 = Set()
        s2 = Set([1,2,2,3]) """

        self.dict = {} 
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """파이썬 프롬프트에서 이 함수를 입력하거나 str() 로 보내주면
        Set 객체를 문자열로 표현해 줌"""
        return "Set: " + str(self.dict.keys())

    # self.dict에서 항목과 True를 각각 key와 value를 사용해서
    # Set 안에 존재하는 항목을 표현
    def add(self, value):
        self.dict[value] = True
    
    # 만약 항목이 dict와 key라면 항목은 Set안에 존재함
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = TestSet([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)

# 여러 함수를 호출할 때 한 함수의 특정 부분을 사용해서 새로운 함수를 만들고 싶을 때가 있다
# 이를 partial function application 또는 currying 이라고 한다
def exp(base, power):
    return base ** power
# 이제 power 라는 변수 한개를 입력하면 exp(2, power) 라는 결과를 출력해 주는 two_to_the 함수를 만들고 싶다고 해보자
def two_to_the(power):
    return exp(2, power)
# 위 방법은 너무 복잡하다

# 대신 functools.partial 이라는 것을 사용
from functools import partial
two_to_the = partial(exp, 2)
print two_to_the(3)

# 인자의 이름을 명시해 주면 뒤에 나오는 인자에도 partial을 적용할 수 있다
square_of = partial(exp, power=2)
print square_of(3)

# 하지만 함수의 중간에 있는 인자를 partial에 사용하면 복잡해질 수 있으니 지양 하자
# 그리고 list comprehension 대안으로 map, reduce, filter를 사용하는 경우도 있다.
def double(x):
    return 2 * x
xs = [1,2,3,4]
twice_xs = [double(x) for x in xs]
print twice_xs
twice_xs = map(double, xs)
print twice_xs
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)
print twice_xs

# 여러개의 list를 입력해 주면 인자가 여러개인 함수에도 map을 적용할수 있다.
def multiply(x, y): return x * y

products = map(multiply, [1,2], [4,5])
print products

# filter는 if가 포함된 list comprehension과 동일
def is_even(x):
    """x가 짝수면 True, 홀수면 False"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
print x_evens
x_evens = filter(is_even, xs)
print x_evens
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)
print x_evens

# reduce는 list의 모든 항목을 순차적으로 합쳐 주면서 list를 하나의 값으로 표현
x_product = reduce(multiply, xs)
print x_product
list_product = partial(reduce, multiply)
x_product = list_product(xs)
print x_product

# list를 반복하면서 list의 항목과 인덱스가 모두 필요한 경우가 종종 있다
# 이 방법은 파이썬 스럽지 않다
documents = ["#data", "#science", "#datascience", "#awesome", "#yolo"]
for i in range(len(documents)):
    document = documents[i]
    print i, document
# 이 방법 또한 파이썬 스럽지 않다
i = 0
for document in documents:
    print i, document
    i += 1
# 가장 파이썬 스러운 방법은 (인덱스, 항목) 형태의 tuple을 생성해 주는 enumerate를 활용 하는 것이다.
for i, document in enumerate(documents):
    print i, document
# 만약 인덱스만 필요하다면 다음과 같이 코드를 작성할 수 있다.
for i in range(len(documents)): print i # 파이썬 스럽지 않다.
for i, _ in enumerate(documents): print i # 파이썬 스럽다

# zip은 여러개의 list를 서로 상응하는 항목의 tuple로 구성된 list로 변환해 준다.
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print zip(list1, list2)
# 주어진 list의 길이가 서로 다른경우 zip은 첫번째 list가 끝나면 멈춘다
list_a = ['a','b','c','d']
list_b = [1,2,3]
print zip(list_b, list_a)
print zip(list_a, list_b)

# 묶인 list는 다음과 같은 트릭을 사용해 다시 풀어줄 수 있다
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print letters
print numbers
# 이 트릭에서 사용한 별표(*) 는 원래 argument unpacking (인자 해체)을 할 때 사용되는 문법
# 이를 사용하면 pairs내의 항목들은 zip 함수에 개별적인 인자로 전달 결국 다음과 같은 코드와 동일
print zip(('a', 1), ('b', 2), ('c', 3))

# 이런 방식의 인자 해체는 모든 함수에 적용할 수 있다.
def add(a, b): return a + b
print add(1, 2)
# add([1, 2]) # TypeError
print add(*[1, 2])

# 특정함수 f를 입력하면 f의 결과를 두배로 만드는 함수를 반환해 주는 고차함수를 만들고 싶다
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g
# 이 함수는 특별한 경우에만 작동
def f1(x):
    return x + 1
g = doubler(f1)
print g(3)
print g(-1)

# 두개 이상의 인자를 받는 함수의 경우에는 문제가 발생
def f2(x, y):
    return x + y
g = doubler(f2)
# print g(1, 2) # TypeError

# 문제를 해결하기 위해 임의의 수의 인자를 받는 함수를 만들어 줘야 한다.
# 앞서 설명한 argument unpacking을 사용하면 마법같이 임의의 수의 인자를 받는 함수를 만들수 있다.
def magic(*args, **kwargs):
    print "unnamed args: ", args
    print "keyword args: ", kwargs
magic(1, 2, key="word", key2="word2")
# 결과
# unnamed args:  (1, 2)
# keyword args:  {'key2': 'word2', 'key': 'word'}
# 위의 함수에서 args는 이름이 없는 인자로 구성된 tuple이며, kwargs 는 이름이 주어진 인자로 구성된 dict이다
# 반대로 정해진 수의 인자가 있는 함수를 호출할 때도 list나 dict로 인자를 전달 할 수 있다.
def other_way_magic(x,y,z):
    print x, y, z
    return x+y+z
x_y_list = [1, 2]
z_dict = {"z" : 3}
print other_way_magic(*x_y_list, **z_dict)

# args와 kwargs를 사용하면 온갖 희한한 것을 할 수 있다. 
# 하지만 앞으로 임의의 인자를 입력 받을 수 있는 고차 함수를 만들 때만 args와 kwargs를 사용할 것이다.
def doubler_correct(f):
    """f의 인자에 상관없이 작동함"""
    def g(*args, **kwargs):
        """g의 인자가 무엇이든 간에 f로 보내줌"""
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print g(1, 2)


