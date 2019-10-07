from collections import defaultdict, Counter
import math

'''
또 다른 흔한 데이터 문제 중 하나는 추천(recommendation)이다.
넷플릭스는 내가 보고 싶어할 법한 영화를 추천해주며
아마존은 사고 싶어할 법한 제품을 추천해준다.
트위터는 팔로우하고 싶어할 만한 사용자들을 추천해 준다.
전에 사용했던 user_interests 데이터에서 추천 시스템 방법론을 몇가지 적
'''

users_interests = [
	["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
	["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
	["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
	["R", "Python", "statistics", "regression", "probability"],
	["machine learning", "regression", "decision trees", "libsvm"],
	["Python", "R", "Java", "C++", "Haskell", "programming languages"],
	["statistics", "probability", "mathematics", "theory"],
	["machine learning", "scikit-learn", "Mahout", "neural networks"],
	["neural networks", "deep learning", "Big Data", "artificial intelligence"],
	["Hadoop", "Java", "MapReduce", "Big Data"],
	["statistics", "R", "statsmodels"],
	["C++", "deep learning", "artificial intelligence", "probability"],
	["pandas", "R", "Python"],
	["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
	["libsvm", "regression", "support vector machines"]
]

'''
수작업을 이용한 추천
예) 책을 추천받고 싶을때 사서에게 책을 추천해 달라고 요청
단점)
	- 사용자의 수가 폭발적으로 많아지면 이 방법을 사용할 수 없음
	- 개인적 지식과 상상력에 의해 제한을 받음 
'''

'''
인기도를 활용한 추천
많은 사람들이 관심을 가지고 있는 항목 중 본인이 해당되지 않는 항목을 추천
'''
popular_interests = Counter(interest
							for user_interests in users_interests
							for interest in user_interests).most_common()

print(popular_interests)


# 사용자가 관심사에 적지 않은 항목들을 전체 인기순으로 사용자에게 추천
def most_popular_new_interests(user_interests, max_results=5):
	suggestions = [(interest, frequency)
				   for interest, frequency in popular_interests
				   if interest not in user_interests]
	return suggestions[:max_results]


print(most_popular_new_interests(users_interests[1], 5))
'''
이 접근은 마케팅 적으로 그리 좋은 방법은 아님,
해당 유저의 정보가 하나도 없을 때 최선일 수도 있으나, 
데이터가 어느정도 축적 되었다면 조금 더 개인화된 추천을 어떻게 할 수 있을지 생각해 봐야함 
'''

'''
사용자의 관심사를 기반으로 추천해 주는 방법 중 하나는, 
특정 사용자 A와 유사한 다른 사용자 B를 찾은 후 B의 관심사를 추천해 주는것

사용자들 간 유사도 정의 : 코사인 유사도(cosine similarity) 지표를 사용
'''


def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def cosine_similarity(v, w):
	return dot(v, w) / math.sqrt(dot(v, v) * dot(w, w))


'''
코사인 유사도는 벡터 v, w 사이의 '각도' 를 잰다. 
만일 v, w 가 완전히 같은 방향을 가리키고 있다면, 분모와 분자가 같은 값을 가지게 되어 코사인 유사도 값은 1이 된다.
정반대는 -1, v는 값이 있더라도 w가 0이면 0 (그 역도 성립)

먼저 사용자들 관심사에 무엇이 있는지 파악하고, 각각의 관심사에 인덱스 번호를 부여
'''

unique_interests = sorted(list({interest
								for user_interests in users_interests
								for interest in user_interests}))

'''
사용자가 해당 관심사를 가지고 있으면 1, 아니면 0 인 벡터를 생성
'''


def make_user_interest_vector(user_interests):
	'''
	unique_interests[i] 의 관심사 list에 존재한다면
	i번째 요소가 1이고, 존재하지 않는다면 0인 벡터 생성
	'''
	return [1 if interest in user_interests else 0
			for interest in unique_interests]


user_interest_matrix = list(map(make_user_interest_vector, users_interests))

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
					  for interest_vector_j in user_interest_matrix]
					 for interest_vector_i in user_interest_matrix]

'''
한 사용자와 가장 유사한 사용자들을 구할 수 있는 함수를 만들수 있다.
본인을 비롯하여, 유사도가 0인 다른 사용자는 반드시 제거
'''


def most_similar_users_to(user_id):
	# 유사도가 0이 아닌 모든 사용자들을 찾고
	pairs = [(other_user_id, similarity)
			 for other_user_id, similarity in
			 enumerate(user_similarities[user_id])
			 if user_id != other_user_id and similarity > 0]

	# 유사도 기준으로 정렬
	return sorted(pairs,
				  key=lambda pair: pair[1],
				  reverse=True)


print(most_similar_users_to(0))

'''
새로운 관심사를 추천해 줄 수 있을까? : 각각의 관심사에 대해 해당 관심사에 관심이 있는 사용자들의 유사도를 모두 더해준다 
'''


def user_based_suggestions(user_id, include_current_interests=False):
	# 모든 유사도를 더함
	suggestions = defaultdict(float)
	for other_user_id, similarity in most_similar_users_to(user_id):
		for interest in users_interests[other_user_id]:
			suggestions[interest] += similarity

	# 정렬된 list로 변환
	suggestions = sorted(suggestions.items(),
						 key=lambda pair: pair[1],
						 reverse=True)

	# (원한다면) 이미 관심사로 표시한 것은 제외한다.
	if include_current_interests:
		return suggestions
	else:
		return [(suggestion, weight)
				for suggestion, weight in suggestions
				if suggestion not in users_interests[user_id]]


print(user_based_suggestions(0))

'''
상품 기반 협업 필터링

관심사 자체에 대한 유사도를 구하는 방법이 있다. 
사용자의 현재 관심사와 가장 유사한 관심사들을 직접적으로 추천해 준다.
기존의 사용자 관심사 행렬의 전치행렬을 구하자, 이 행렬은 관심사가 행 사용자가 열이 된다.
'''
interest_user_matrix = [[user_interest_vector[j]
						 for user_interest_vector in user_interest_matrix]
						for j, _ in enumerate(unique_interests)]

print(unique_interests)
print(interest_user_matrix[0])

'''
코사인 유사도 적용, 완전히 동일한 사용자들의 집합이 두 관심사에 관심이 있다면 이 관심사들의 유사도는 1이다.
'''
interest_similarities = [[cosine_similarity(user_vector_i, user_vector_j)
						  for user_vector_j in interest_user_matrix]
						 for user_vector_i in interest_user_matrix]
print(interest_similarities)

'''
interest 0 인 Big Data와 (unique_interests[0]) 가장 유사한 관심사는 다음 함수를 이용해서 구할 수 있다.
'''


def most_similar_interests_to(interest_id):
	similarities = interest_similarities[interest_id]
	pairs = [(unique_interests[other_interest_id], similarity)
			 for other_interest_id, similarity in enumerate(similarities)
			 if interest_id != other_interest_id and similarity > 0]
	return sorted(pairs,
				  key=lambda pair: pair[1],
				  reverse=True)


print(most_similar_interests_to(0))

'''
추천 목록은, 사용자의 관심사와 유사한 관심사들의 유사도의 합으로 구할 수 있다.
'''


def item_based_suggestions(user_id, include_current_interests=False):
	# 비슷한 관심사를 더함
	suggestions = defaultdict(float)
	user_interest_vector = user_interest_matrix[user_id]
	for interest_id, is_interested in enumerate(user_interest_vector):
		if is_interested == 1:
			similar_interests = most_similar_interests_to(interest_id)
			for interest, similarity in similar_interests:
				suggestions[interest] += similarity

	# 가중치 기준으로 정렬
	suggestions = sorted(suggestions.items(),
						 key=lambda pair: pair[1],
						 reverse=True
						 )

	# 이미 있는 관심사 제외
	if include_current_interests:
		return suggestions
	else:
		return [(suggestion, weight)
				for suggestion, weight in suggestions
				if suggestion not in users_interests[user_id]]


item_based_suggestions(0)
