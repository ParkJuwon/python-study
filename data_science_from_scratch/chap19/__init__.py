import random
from functools import reduce
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

'''
레이블이 있는 데이터로 모델을 학습해서 레이블이 없는 데이터의 레이블을 예측한다는 점에서 지도학습(supervised learning)
알고리즘이라고 한다. 하지만 군집화(clustering)는 레이블이 없는 데이터를 사용하는, 또는 레이블이 있더라도 그것을 사용하지 않는
비지도 학습(unsupervised learning)의 일종이다.
'''

'''
가장 간단한 군집화 방법 중 하나는 군집의 개수 k를 미리 정해두는 k-means 이다.
이 알고리즘은 데이터와 데이터가 속한 군집의 중심점과의 거리의 제곱합을 최소화시키며 S1,...,Sk까지 군집을 구한다.

n개의 데이터 포인트를 할당하는 방법은 아주 다양하다. 최적의 군집을 찾는 것은 무척 어렵다.

반복 연산으로 제법 좋은 군집을 찾는 방법
1. d-차원 공간에서 임의의 점 k개를 찍고, 이들은 각 군집의 중심점으로 간주
2. 각 데이터 포인트에서 가장 가까운 중심점을 기준으로 군집을 설정
3. 소속된 군집이 바뀐 데이터 포인트가 하나도 없다면, 군집을 기록하고 종료
4. 소속된 군집이 바뀐 데이터 포인트가 하나라도 있다면, 중심점을 다시 계산하고 2단계로 돌아간다.
'''


def vector_add(v, w):
	"""adds two vectors componentwise"""
	return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
	"""subtracts two vectors componentwise"""
	return [v_i - w_i for v_i, w_i in zip(v, w)]


def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)


def squared_distance(v, w):
	return sum_of_squares(vector_subtract(v, w))


def vector_sum(vectors):
	return reduce(vector_add, vectors)


def scalar_multiply(c, v):
	return [c * v_i for v_i in v]


def vector_mean(vectors):
	"""compute the vector whose i-th element is the mean of the
	i-th elements of the input vectors"""
	n = len(vectors)
	return scalar_multiply(1 / n, vector_sum(vectors))


class KMeans:
	"""k-means로 군집화 실행"""

	def __init__(self, k):
		self.k = k  # 군집의 개수
		self.means = None  # 군집의 중심

	def classify(self, input):
		"""입력 데이터에 가장 인접한 군집의 인덱스를 반환"""
		return min(range(self.k),
				   key=lambda i: squared_distance(input, self.means[i]))

	def train(self, inputs):
		# 임의로 k개의 점을 초기 중심점으로 선택
		self.means = random.sample(inputs, self.k)
		assignments = None

		while True:
			# 소속되는 군집을 다시 찾기
			new_assignments = map(self.classify, inputs)

			# 소속되는 군집이 바귀지 않았다면 종료
			if assignments == new_assignments:
				return

			# 아니면 새로운 군집을 찾기
			assignments = new_assignments

			# 수정된 군집의 새로운 중심점 계산
			for i in range(self.k):
				# 군집 i에 속하는 모든 데이터 탐색
				i_points = [p for p, a in zip(inputs, assignments) if a == i]

				# 0으로 나누는 일이 없도록 i_points 가 비어 있지 않는지 확인
				if i_points:
					self.means[i] = vector_mean(i_points)


'''
k 값 선택하기
앞의 예시에서는 외부 요인이 k 값을 결정했지만, 그런 경우는 보통 드물다. k 값을 정할 수 있는 방법은 매우 다양하다.
쉬운 방법 중 하나는 k 값에 대해 중심 점과 각 데이터 포인트 사이의 거리의 제곱합을 그래프로 그리고,
그 그래프가 어디서 꺾이는지 관찰하는 것이다.
'''


def squared_clustering_errors(inputs, k):
	"""inputs에 대해 k-means 군집화 실행하고 총 오류 제곱 값을 계산"""
	cluster = KMeans(k)
	cluster.train(inputs)
	means = cluster.means
	assignments = map(cluster.classify, inputs)

	return sum(squared_distance(input, means[cluster])
			   for input, cluster in zip(inputs, assignments))

'''
상향식 군집들을 묶는 방법이 있다.
다음과 같은 방법으로 처리
1. 각 데이터 포인트를 하나의 군집으로 간주
2. 군집이 두 개 이상이라면, 가장 가까운 두 개의 군집을 찾아 하나의 군집으로 묶음

위의 반복 연산이 완전히 종료되면, 최종적으로 단 하나의 거대한 군집만이 남게 된다
다만, 군집들을 묶어 나가는 중간 과정을 모두 기록해 두기 때문에, 언제든 묶인 군집을 다시 풀 수 있다.
예를 들어, 세 개의 군집을 원한다면 마지막 두번의 병합만 돌리면 된다

군집을 표현할 때는 간단한 표기법을 쓰자. 
데이터 값을 항목의 수가 한 개인 '잎(leaf) 군집(tuple)' 에 넣도록 하자
'''


if __name__ == "__main__":
	img = mpimg.imread(r"test.png")
	top_row = img[0]
	top_left_pixel = top_row[0]

	# red, green, blue = top_left_pixel
	pixels = [pixel for row in img for pixel in row]

	clusterer = KMeans(5)
	clusterer.train(pixels)  # 이부분은 조금 오래 걸릴수 있다


	def recolor(pixel):
		cluster = clusterer.classify(pixel)  # 가장 가까운 군집의 인덱스
		return clusterer.means[cluster]  # 가장 가까운 군집의 중심값


	new_img = [[recolor(pixel) for pixel in row]  # 해당 픽셀 행을 다시 칠함
			   for row in img]  # 이미지의 모든 행에 대해

	plt.imshow(new_img)
	plt.axis('off')
	plt.show()
