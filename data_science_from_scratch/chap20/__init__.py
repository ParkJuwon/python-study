import matplotlib.pyplot as plt
import re
import requests, random
from bs4 import BeautifulSoup
from collections import defaultdict, Counter

data = [("big data", 100, 15), ("Hadoop", 95, 25), ("Python", 75, 50),
		("R", 50, 40), ("machine learning", 80, 20), ("statistics", 20, 60),
		("data science", 60, 70), ("analytics", 90, 3),
		("team player", 85, 85), ("dynamic", 2, 90), ("synergies", 70, 0),
		("actionable insights", 40, 30), ("think out of the box", 45, 10),
		("self-starter", 30, 50), ("customer focus", 65, 15),
		("thought leadership", 35, 35)]


def text_size(total):
	"""total 이 0 이라면 8을 반환. 200이라면 28을 반환."""
	return 8 + total / 200 * 20


'''
워드 클라우드
멋있어 보이긴 하지만 딱히 어떤 정보를 제공하지 않음
'''
for word, job_popularity, resume_popularity in data:
	plt.text(job_popularity, resume_popularity, word,
			 ha='center', va='center',
			 size=text_size(job_popularity + resume_popularity))
plt.xlabel("Popularity on Job Postings")
plt.ylabel("Popularity on Resumes")
plt.axis([0, 100, 0, 100])
# plt.show()

'''
n-gram 모델
'''


def fix_unicode(text):
	return text.replace(u"\u2019", "'")


# url = 'http://radar.oreilly.com/2010/06/what-is-data-science.html'
urls = ['https://blog.naver.com/PostView.nhn?blogId=ehaulee&logNo=221659854277&redirect=Dlog&widgetTypeCall=true&directAccess=false',
		'https://blog.naver.com/PostView.nhn?blogId=soo_420&logNo=221656106305&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FBlogHome.nhn%3FdirectoryNo%3D0%26currentPage%3D1%26groupId%3D0&directAccess=false',
		'https://blog.naver.com/PostView.nhn?blogId=betty9156&logNo=221653611926&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FBlogHome.nhn%3FdirectoryNo%3D0%26currentPage%3D1%26groupId%3D0&directAccess=false',
		'https://blog.naver.com/PostView.nhn?blogId=lysenef&logNo=221659661792&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FThisMonthDirectory.nhn&directAccess=false',
		'https://blog.naver.com/PostView.nhn?blogId=redfox0127&logNo=221659972178&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FThisMonthDirectory.nhn&directAccess=false',
		'https://blog.naver.com/PostView.nhn?blogId=hollyforest&logNo=221658418640&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FThisMonthDirectory.nhn&directAccess=false',
		'https://blog.naver.com/PostView.nhn?blogId=tazan00009&logNo=221659446008&redirect=Dlog&widgetTypeCall=true&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FThisMonthDirectory.nhn&directAccess=false',
		'https://blog.naver.com/PostList.nhn?blogId=huck15&widgetTypeCall=true&categoryNo=27&from=section&topReferer=https%3A%2F%2Fsection.blog.naver.com%2FThisMonthDirectory.nhn%3Fyear%3D2019%26month%3D7&directAccess=true'
		]

contents = []

for url in urls:
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'html5lib')
	content = soup.findAll('p', 'se-text-paragraph')
	contents += content

# content = soup.find('div', 'post-radar-content') # entry-content div 찾아줌

regex = r"[\w']+|[\.]"  # 단어나 마침표에 해당하는 문자열

document = []
# for paragraph in content('p'):
# 	words = re.findall(regex, fix_unicode(paragraph.text))
# 	document.extend(words)

for content in contents:
	for paragraph in content('span'):
		words = re.findall(regex, fix_unicode(paragraph.text))
		document.extend(words)

print(document)
'''
어떤 단어 다음으로 등장할 법한 단어를 임의로 선택하고, 문장의 끝을 의미하는 마침표가 등장할 때까지 이 과정을 무한히 반복
이 과정을 2-gram 또는 바이그램(bigram) 모델이라 부른다.
바이그램 모델은 데이터에 등장하는 바이그램의 빈도를 통해 언어를 모델링
'''

biagram = zip(document, document[1:])
transitions = defaultdict(list)
for prev, current in biagram:
	transitions[prev].append(current)

print(transitions)


def generate_using_bigrams(transitions):
	current = "."  # 이 뜻은 다음 단어가 문장의 시작이라는 것을 의미
	result = []
	while True:
		next_word_candidates = transitions[current]  # biagrams (current, ...)
		if next_word_candidates:
			current = random.choice(next_word_candidates)  # 임의로 하나 선택
			result.append(current)  # result에 추가
			if current == ".":
				data = " ".join(result)  # 만약 "." 라면 종료
				if len(data) > 20:
					return data
		else:
			break


# random.seed(0)
print("bigram sentences")
for i in range(10):
	print(i, generate_using_bigrams(transitions))
print()

'''
바이그램 모델이 아니라 3개의 연속적인 단어를 보는 트리이그램(trigram) 모델을 사용하면 문장은 더욱 그럴듯한 형태가 될 것이다
(물론 n개의 연속적인 단어를 보는 n-gram을 사용할 수도 있겠지만, 보통 3개 정도만 봐도 충분
'''
trigrams = zip(document, document[1:], document[2:])
trigram_transitions = defaultdict(list)
starts = []
for prev, current, next in trigrams:
	if prev == ".":  # 만약 이전단어가 마침표였다면
		starts.append(current)  # 이제 새로운 단어의 시작을 의미

	trigram_transitions[(prev, current)].append(next)


def generate_using_trigrams(starts, trigram_transitions):
	current = random.choice(starts)  # 임의의 시작 단어를 선택
	prev = "."  # 앞에 '.' 를 추가
	result = [current]
	while True:
		next_word_candidates = trigram_transitions[(prev, current)]
		if next_word_candidates:
			next = random.choice(next_word_candidates)

			prev, current = current, next
			result.append(current)

			if current == ".":
				data = " ".join(result)  # 만약 "." 라면 종료
				if len(data) > 20:
					return data
		else:
			break


print("trigram sentences")
for i in range(10):
	print(i, generate_using_trigrams(starts, trigram_transitions))
print()


'''
깁스 샘플링(gibbs sampling)이란 일부 조건부 확률분포만 알고 있을 때 다차원 분포로부터 표본을 얻을 수 있는 방법이다.
'''