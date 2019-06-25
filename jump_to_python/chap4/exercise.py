# 함수
## Q1
def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	return fib(n - 1) + fib(n - 2)


# 파일 읽고 쓰기
## Q1
f = open("sample.txt", 'r')
lines = f.readlines()
f.close()

total = 0
for line in lines:
	score = int(line)
	total += score

average = total / len(line)
f = open("result.txt", "w")

f.write("%d\t%d" % (total, average))

f.close()