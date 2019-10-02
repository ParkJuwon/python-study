import matplotlib.pyplot as plt
import networkx as nx
from functools import partial
import random, math


def draw_graph(input_G, layout="shell"):
	if layout == "shell":
		pos = nx.shell_layout(input_G)
	elif layout == "spring":
		pos = nx.spring_layout(input_G)
	elif layout == "spectral":
		pos = nx.spectral_layout(input_G)
	elif layout == "circular":
		pos = nx.circular_layout(input_G)
	elif layout == "random":
		pos = nx.random_layout(input_G)
	else:
		pos = nx.shell_layout(input_G)

	plt.figure()
	nx.draw_networkx_nodes(input_G, pos)
	nx.draw_networkx_edges(input_G, pos)
	nx.draw_networkx_labels(input_G, pos)
	nx.draw_networkx_edge_labels(input_G, pos)
	plt.show()


'''
많은 데이터 문제는 노드(node)와 그 사이를 연결하는 엣지(edge)로 구성된 네트워크(network) 관점에서 볼수 있다.

1. undirected network: 방향이 없는 네트워크
	- 페이스북의 친구 관계 (상호적) - A가 B의 친구라면 B는 A의 친구다
2. directed network: 방향이 있는 네트워크
	- 하이퍼링크
'''

'''
매개 중심성
1장, 데이텀 네트워크에서 친구 수를 셈으로써 중심이 되는 주요 핵심 인물을 찾았다.
몇가지 추가적인 접근법을 살펴보자
'''

users = [
	{"id": 0, "name": "Hero"},
	{"id": 1, "name": "Dunn"},
	{"id": 2, "name": "Sue"},
	{"id": 3, "name": "Chi"},
	{"id": 4, "name": "Thor"},
	{"id": 5, "name": "Clive"},
	{"id": 6, "name": "Hicks"},
	{"id": 7, "name": "Devin"},
	{"id": 8, "name": "Kate"},
	{"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
			   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# graph 출력
G = nx.Graph()
G.add_edges_from(friendships)
draw_graph(G)

for user in users:
	user["friends"] = []

for i, j in friendships:
	# users[i]는 사용자 중 id가 i인 사람을 의미하기 때문에 문제없이 작동한다
	users[i]["friends"].append(users[j])  # j를 i의 친구로 추가
	users[j]["friends"].append(users[i])  # i를 j의 친구로 추가

'''
1장에서 연결 중심성(degree centrality)을 살펴볼 때, 직관적으로 생각했던 주요 연결고리들이 선정되지 않았음
대안으로 사용할 수 있는 지수 중 하나는 매개 중심성(betweenness centrality) 이다.
	- 이는 임의의 두 사람 사이의 최단 경로상에 빈번하게 등장하는 사람들이 큰 값을 가지는 지수
	- 구체적으로는, 노드 i의 매개 중심성은 다른 노드 j,k 쌍의 최단 경로 중에, i를 거치는 경로의 비율로 계산.

첫번째로 할 수 있는 것은 임의의 두 사람이 주어졌을 때 그들 간의 최단 경로를 모두 구하는 것
'Breadth-first search'(너비 우선 탐색, BFS) 라고도 알려져 있는 알고리즘 사용 (그래도 이 책에서는 가장 복잡한 알고리즘 중 하나)
'''

from collections import deque


def shortest_paths_from(from_user):
	# 특정 사용자로부터 다른 사용자까지의 모든 최단 경로를 포함하는 dict
	shortest_paths_to = {from_user["id"]: [[]]}

	# 확인해야 하는 (이전 사용자, 다음 사용자) 큐
	# 모든 (from_user, from_user의 친구) 쌍으로 시작
	frontier = deque((from_user, friend)
					 for friend in from_user["friends"])

	# 큐가 빌 때까지 반복
	while frontier:

		prev_user, user = frontier.popleft()  # 큐의 첫 번째 사용자를 가져옴
		user_id = user['id']

		# 큐에 사용자를 추가하는 방법을 고려해 보면
		# prev_user 까지의 최단 경로를 이미 알고 있을 수도 있다.
		paths_to_prev_user = shortest_paths_to[prev_user["id"]]
		new_paths_to_user = [path + [user_id] for path in paths_to_prev_user]

		# 만약 최단 경로를 이미 알고 있다면
		old_paths_to_user = shortest_paths_to.get(user_id, [])

		# 지금까지의 최단 경로는 무엇일까?
		if old_paths_to_user:
			min_path_length = len(old_paths_to_user[0])
		else:
			min_path_length = float('inf')

		# 길지 않은 새로운 경로만 저장
		new_paths_to_user = [path
							 for path in new_paths_to_user
							 if len(path) <= min_path_length
							 and path not in old_paths_to_user]

		shortest_paths_to[user_id] = old_paths_to_user + new_paths_to_user

		# 아직 한번도 보지 못한 이웃을 frontier 에 추가
		frontier.extend((user, friend)
						for friend in user["friends"]
						if friend["id"] not in shortest_paths_to)

	return shortest_paths_to


for user in users:
	user["shortest_paths"] = shortest_paths_from(user)

for user in users:
	user["betweenness_centrality"] = 0.0

for source in users:
	source_id = source['id']
	for target_id, paths in source["shortest_paths"].items():
		if source_id < target_id:  # 잘못해서 두 번 세지 않도록 주의
			num_paths = len(paths)  # 최단 경로가 몇 개 존재하는가?
			contrib = 1 / num_paths  # 중심성에 기여하는 값
			for path in paths:
				for id in path:
					if id not in [source_id, target_id]:
						users[id]["betweenness_centrality"] += contrib

'''
근접 중심성(closeness centrality)
	- 각 사용자의 원접성(farness) 을 계산, 원접성이란 from_user 와 다른 모든 사용자의 최단 경로를 합한 값
	(만약 여러 개의 최단 경로를 찾았다면 어차피 모든 최단 경로의 거리는 동일하니 첫 번째 최단 경로의 거리만 더해 주자)
'''


def farness(user):
	'''모든 사용자와의 최단 거리 합'''
	return sum(len(paths[0])
			   for paths in user["shortest_paths"].values())


for user in users:
	user['closeness_centrality'] = 1 / farness(user)

'''
고유벡터 중심성

행렬 연산
A가 n1 x k1 행렬, B가 n2 x k2 행렬 그리고 k1 = n2 라고 하면 
두 행렬의 곱 AB는 n1 x k2 행렬이 되고, 이때 (i, j) 번째 항목의 값은 다음과 같다.
Ai1Bij + Ai2B2j + ... + AikBkj
'''


def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def get_row(A, i):
	return A[i]


def get_column(A, j):
	return [A_i[j] for A_i in A]


# 이는 A의 i 번째 행과 B의 j 번째 열의 내적과 동일하다.
def matrix_product_entry(A, B, i, j):
	return dot(get_row(A, i), get_column(B, j))


def shape(A):
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0
	return num_rows, num_cols


def make_matrix(num_rows, num_cols, entry_fn):
	"""returns a num_rows x num_cols matrix
	whose (i,j)-th entry is entry_fn(i, j)"""
	return [[entry_fn(i, j) for j in range(num_cols)]
			for i in range(num_rows)]


# 이를 이용해 행렬의 곱을 다음과 같이 계산할 수 있다.
def matrix_multiply(A, B):
	n1, k1 = shape(A)
	n2, k2 = shape(B)
	if k1 != n2:
		raise ArithmeticError("incompatible shapes!")

	return make_matrix(n1, k2, partial(matrix_product_entry, A, B))


# 이에 따라 A 가 n x k 행렬이고 B가 k x l 행렬일 때 AB는 n x l 행렬이 된다.

# 벡터 표현 방법을 서로 변환해 주는 함수
def vector_as_matrix(v):
	"""list 형태의 벡터 v를 n x 1 행렬로 변환"""
	return [[v_i] for v_i in v]


def vector_from_matrix(v_as_matrix):
	"""n x 1 행렬을 list 로 변환"""
	return [row[0] for row in v_as_matrix]


# matrix_multiply를 동원하여 행렬 연산을 정의
def matrix_operate(A, v):
	v_as_matrix = vector_as_matrix(v)
	product = matrix_multiply(A, v_as_matrix)
	return vector_from_matrix(product)


'''
A가 사각행렬(square matrix)이라면 이 연산은 n차원 벡터를 다른 n차원 벡터로 변환
때로는 A와 v의 값에 따라 A와 v를 곱하면 v의 상수 배에 해당하는 벡터를 얻을 때가 있다.
즉, 결과값으로 나온 벡터는 기존 벡터 v와 같은 방향을 가리키는 벡터가 된다는 것을 의미.
v가 0으로만 이뤄진 벡터가 아닌데도 이런 일이 생기면 v를 A의 고유벡터(eigenvector)라고 부르고,
이때 곱해진 상수를 고유값(eigenvalue)이라고 부르게 된다.

행렬 A의 고유백터를 찾는 방법은, 임의의 벡터 v를 골라 matrix_operate를 수행하고, 
결과값의 크기가 1이 되게 재조정 하는 과정을 반복 수행하는 것이다. 
'''


def sum_of_squares(v):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)


def magnitude(v):
	return math.sqrt(sum_of_squares(v))


def scalar_multiply(c, v):
	return [c * v_i for v_i in v]


def vector_subtract(v, w):
	"""subtracts two vectors componentwise"""
	return [v_i - w_i for v_i, w_i in zip(v, w)]


def squared_distance(v, w):
	return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
	return math.sqrt(squared_distance(v, w))


def find_eigenvector(A, tolerance=0.0001):
	guess = [random.random() for __ in A]

	while True:
		result = matrix_operate(A, guess)
		length = magnitude(result)
		next_guess = scalar_multiply(1 / length, result)

		if distance(guess, next_guess) < tolerance:
			return next_guess, length  # 고유벡터, 고유값

		guess = next_guess


'''
결과값으로 반환되는 guess 를 matrix_operate를 통해 결과값의 크기가 1인 벡터로 재조정하면, 자기 자신이 반환된다.
즉, 여기서 guess는 고유벡터라는 것을 의미한다.
'''

'''
모든 실수 행렬에 고유벡터와 고유값이 있는 것은 아니다.
예를 들어 시계 방향으로 90도 회전하는 연산을 하는 다음 행렬에는 곱했을 때 자기 자신이 되는 벡터는 영벡터밖에 없다. 
'''
rotate = [[0, 1],
		  [-1, 0]]  # 이 행렬로 앞에 구현한 find_eigenvector 를 수행하면 영원히 끝나지 않는다.

# 고유벡터가 있는 행렬도 때로는 무한루프에 빠질 수 있음
flip = [[0, 1],
		[1, 0]]
'''
이 행렬은 모든 벡터 [x, y]를 [y, x]로 변환 
하지만 x, y 값이 다른 임의의 벡터에서 출발해서 find_eigenvector 를 수행하면 
x, y 값을 바꾸는 연산만 무한히 수행할 것이다.
(numpy 같은경우 이런 케이스까지 다루는 다양한 방법이 있음)

결과적으로  find_eigenvector 가 결과값을 반환하면 그 결과 값은 곧 고유벡터
'''

'''
중심성
고유벡터가 데이텀 네트워크를 이해하는 데 어떻게 도움을 줄까?
- 네트워크를 인접행렬(adjacency matrix)의 형태로 나타내 봄
- 이 행렬은 사용자 i와 사용자 j가 친구인 경우 (i, j)번째 항목에 1이 있고 친구가 아닌경우 0이 있는 행렬이다.
'''


def entry_fn(i, j):
	return 1 if (i, j) in friendships or (j, i) in friendships else 0


n = len(users)
adjacency_matrix = make_matrix(n, n, entry_fn)

'''
각 사용자의 고유벡터 중심성이란 find_eigenvector 로 찾은 사용자의 고유벡터가 된다.
'''
eigenvector_centralities, _ = find_eigenvector(adjacency_matrix)

'''
연결 수가 많고, 중심성이 높은 사용자들한데 연결된 사용자들은 고유벡터 중심성이 높다.
'''

'''
아직 고유벡터가 중심성과 어떠한 관련이 있는지 얘기하진 않았.
고유벡터는 다음의 값을 계산했을 때 결과값이 eigenvector_centralities의 상수배가 된다.
'''
matrix_operate(adjacency_matrix, eigenvector_centralities)

'''
행렬곱이 어떻게 동작하는지 살펴보면 matrix_operate는 i번째 항목으로 
다음의 값을 가지는 벡터를 계산해 준다는 것을 알수 있다
'''
dot(get_row(adjacency_matrix, i), eigenvector_centralities)
'''
이 값은 사용자 i에게 연결되어 있는 사용자들의 eigenvector_centralities의 합과 같다.
바꿔 말하면, 고유벡터 중심성은 사용자 당 하나씩 부여되는 숫자 그 숫자는 이웃의 중심성의 합의 배수.
이 경우 중심성이란, 중심성이 높은 사람들과 연결되어 있는 정도를 의미
즉 중심성이 높은 사람들과 많이 연결되어 있을수록 자신의 중심성도 높다.
'''

'''
find_eigenvector의 역할에 대해 생각, 이 현상을 다른관점에서 해석
find_eigenvector는 각 노드에 임의의 중심성을 할당하는 것으로 시작해서, 다음 두 단계가 수렴할 때까지 반복
	1. 각 노드의 이웃에 있는 중심성 점수의 합으로 해당 노드에 새로운 중심성 점수를 부여
	2. 중심성 벡터의 크기가 1이 되도록 벡터를 재조정
'''

'''
방향성 그래프(Directed graphs)와 페이지랭크
친구 모델에서 보증 모델로 
이 새로운 모델에서 관계는 상호적인 것이 아니라, 한사람(source)이 다른 멋진사람(target)의 실력에 보증을 서주는
(source, target) 쌍으로 비대칭적인 관계를 표현
'''
endorsements = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1), (1, 3),
				(2, 3), (3, 4), (5, 4), (5, 6), (7, 5), (6, 8), (8, 7), (8, 9)]

for user in users:
	user["endorses"] = []  # 다른 사람을 보증해 주는 정보를 유지하기 위해 list를 생성
	user["endorsed_by"] = []  # 보증을 받는 것에 대한 정보를 유지하기 위해 새로운 list를 생성

for source_id, target_id in endorsements:
	users[source_id]["endorses"].append(users[target_id])
	users[target_id]["endorsed_by"].append(users[source_id])

endorsements_by_id = [(user["id"], len(user["endorsed_by"]))
					  for user in users]

sorted(endorsements_by_id, key=lambda pair: pair[1], reverse=True)

'''
'보증의 수' 같은 숫자는 조작이 매우 쉬움
좀더 나은 지수는 '누가' 보증을 서는지를 고려
그것이 페이지랭크(PageRank) 알고리즘의 기본 철학이기도 함
	1. 네트워크 전체에는 1.0(또는 100%)의 페이지 랭크가 있다.
	2. 초기에 이 페이지랭크를 모든 노드에 고르게 배당한다.
	3. 각 스텝을 거칠 때마다 각 노드에 배당된 페이지랭크의 대부분은 외부로 향하는 링크에 균등하게 배당
	4. 각 스텝을 거칠 때마다 각 노드에 남아 있는 페이지랭크를 모든 노드에 고르게 배당 
'''

def page_rank(users, damping = 0.85, num_iters = 100):

	# 먼제 페이지랭크를 모든 노드에 고르게 배당
	num_users = len(users)
	pr = {user["id"] : 1 / num_users for user in users}

	# 매 스텝마다 각 노드가 받는
	# 적은 량의 PageRank
	base_pr = (1 - damping) / num_users

	for __ in range(num_iters):
		next_pr = {user["id"]: base_pr for user in users}
		for user in users:
			# 페이지랭크를 외부로 향하는 링크에 배당한다
			links_pr = pr[user["id"]] * damping
			for endorsee in user["endorses"]:
				next_pr[endorsee["id"]] += links_pr / len(user["endorses"])
			pr = next_pr

	return pr

'''
더 공부해 보고 싶다면
- 이곳에서 언급한 중심성 지표들은 가장 인기 있는 것들이기는 하지만, 언급하지 않은 다른 중심성 지표들도 있다.
- networkX는 네트워크 분석을 위한 파이썬 라이브러리다. 중심성을 계산 하거나 그레프를 시각화하는 데 사용할 수 있다.
- Gephi는 애증이 깃든 GUI 기반의 네트워크 시각화 도구이
'''
