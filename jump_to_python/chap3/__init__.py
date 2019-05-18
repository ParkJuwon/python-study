# and, or, not

money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# x in s, x not in s
print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ('a','b','c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 조건문 실행에 따라 아무일을 않하게 설정하고 싶을떄
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass # pass 수행 아무것도 하지않음
else:
    print("걸어가라")


pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


#
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number: """
#
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)


# range
a = range(10)
print(a)

a = range(1, 11)
print(a)

sum = 0
for i in range(1,11):
    sum = sum + i

print(sum)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("{0}번 학생 축하합니다 합격입니다".format(number + 1))


# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ") # end를 붙혀 다음줄로 넘기지 않고 공백으로 바꿔줌
    print('')


# 리스트 안에 for문 포함시키기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result)

# 리스트 내포를 이용
result = [num * 4 for num in a]
print(result)

# [ 표현식 for 항목 in 반복가능객체 if 조건 ]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

"""
 [표현식 for 항목1 in 반복가능객체1 if 조건1
    for 항목2 in 반복가능객체2 if 조건2
    ...
    for 항목n in 반복가능객체n if 조건n
"""
result = [x*y for x in range(2,10)
          for y in range(1,10)]

print(result)






