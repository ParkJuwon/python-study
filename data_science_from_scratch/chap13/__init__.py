import glob
import math
import random
import re
from collections import Counter
from collections import defaultdict

from machine_learning import split_data


def tokenize(message):
	message = message.lower()
	all_words = re.findall("[a-z0-9]+", message)
	return set(all_words)


def count_words(training_set):
	"""학습 데이터는 (메시지 내용, 스팸 여부) 형식으로 구성되어 있음"""
	counts = defaultdict(lambda: [0, 0])
	for message, is_spam in training_set:
		for words in tokenize(message):
			counts[words][0 if is_spam else 1] += 1
	return counts


def word_probabilities(counts, total_spams, total_non_spams, k=0.5):
	"""단어의 빈도수를
	[단어, p(w|스팸), p(w|~스팸)] 형태로 변환"""
	return [(w,
			 (spam + k) / (total_spams + 2 * k),
			 (non_spam + k) / (total_non_spams + 2 * k))
			for w, (spam, non_spam) in counts.items()]


def spam_probability(word_probs, message):
	message_words = tokenize(message)
	log_prob_if_spam = log_prob_if_not_spam = 0.0

	# 모든 단어에 대해 반복
	for word, prob_if_spam, prob_if_not_spam in word_probs:

		# 만약 메시지에 word 가 나타나면
		# 해당 단어가 나올 log 확률을 더해 줌
		if word in message_words:
			log_prob_if_spam += math.log(prob_if_spam)
			log_prob_if_not_spam += math.log(prob_if_not_spam)

		# 만약 메시지에 word가 나타나지 않는다면
		# 해당 단어가 나오지 않을 log 확률을 더해 줌
		# 나오지 않는 확률은 log(1 - 나올확률) 로 계산
		else:
			log_prob_if_spam += math.log(1.0 - prob_if_spam)
			log_prob_if_not_spam += math.log(1.0 - prob_if_not_spam)

	prob_if_spam = math.exp(log_prob_if_spam)
	prob_if_not_spam = math.exp(log_prob_if_not_spam)
	return prob_if_spam / (prob_if_spam + prob_if_not_spam)


class NaiveBayesClassfier:

	def __init__(self, k=0.5):
		self.k = k
		self.word_probs = []

	def train(self, training_set):
		# 스팸 메시지와 스팸이 아닌 메시지의 개수를 세어 줌
		num_spams = len([is_spam
						 for message, is_spam in training_set
						 if is_spam])
		num_non_spams = len(training_set) - num_spams

		# 지금까지 만든 함수에 학습 데이터를 적용
		word_counts = count_words(training_set)
		self.word_probs = word_probabilities(word_counts,
											 num_spams,
											 num_non_spams,
											 self.k)

	def classify(self, message):
		return spam_probability(self.word_probs, message)


def get_subject_data():
	# 실제 파일을 저장한 경로로 path를 바꿔 주자
	path = "spam_mail/*/*"

	data = []

	# glob.glob은 주어진 경로에 해당하는 모든 파일 이름을 반환
	for fn in glob.glob(path):
		is_spam = "ham" not in fn

		with open(fn, 'r', encoding='ISO-8859-1') as file:
			for line in file:
				if line.startswith("Subject:"):
					# Subject 부분을 제거하고 나머지 부분을 유지
					subject = re.sub(r"^Subject: ", "", line).strip()
					data.append((subject, is_spam))
	return data


def p_spam_given_word(word_prob):
	"""베이즈 정리를 통해 p(스팸 \ 메시지가 해당 단어를 포함) 을 계산"""
	word, prob_if_spam, prob_if_not_spam = word_prob
	return prob_if_spam / (prob_if_spam + prob_if_not_spam)


if __name__ == "__main__":
	data = get_subject_data()
	random.seed(0)  # 예시와 동일한 결과를 얻기위해 설정
	train_data, test_data = split_data(data, 0.75)

	classifier = NaiveBayesClassfier()
	classifier.train(train_data)

	classified = [(subject, is_spam, classifier.classify(subject))
				  for subject, is_spam in test_data]

	counts = Counter((is_spam, spam_probability > 0.5)  # (actual, predicted)
					 for _, is_spam, spam_probability in classified)
	print(counts)

	# 스팸일 확률을 오름차순으로 정렬
	classified.sort(key=lambda row: row[2])

	# 스팸이 아닌 메시지 중에서 스팸일 확률이 가장 높은 메시지
	spammiest_hams = list(filter(lambda row: not row[1], classified))[-5:]

	# 스팸 중에서 스팸일 가장 낮은 메시지
	hammiest_spams = list(filter(lambda row: row[1], classified))[:5]

	print("spammiest_hams", spammiest_hams)
	print("hammiest_spams", hammiest_spams)

	words = sorted(classifier.word_probs, key=p_spam_given_word)

	spammiest_words = words[-5:]
	hammiest_words = words[:5]

	print("spammiest_words", spammiest_words)
	print("hammiest_words", hammiest_words)
