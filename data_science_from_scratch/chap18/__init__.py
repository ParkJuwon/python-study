import math, random

'''
퍼셉트론은 n 개의 이진수가 하나의 뉴런을 통과해서 가중합이 0보다 크면 활성화되는 가장 간단한 신경망 구조이
'''


def step_function(x):
	return 1 if x >= 0 else 0


def dot(v, w):
	"""v_1 * w_1 + ... + v_n * w_n"""
	return sum(v_i * w_i for v_i, w_i in zip(v, w))


def perceptron_output(weights, bias, x):
	"""returns 1 if the perceptron 'fires', 0 if not"""
	return step_function(dot(weights, x) + bias)


'''
인공 신경망으로 뇌를 묘사할 때는 여러개의 연속된 층으로 추상화하는 것이 일반적이다.
보통은 입력값을 받고 그대로 다음층으로 값을 전송하는 입력층(input layer), 하나 이상의 은닉층 (hidden layer),
그리고 최종값을 반환하는 출력층(output layer) 등으로 구성한다.
은닉층은 직전층의 출력값을 입력 받아 어떤 계산을 하고 다음층으로 전달하는 역할을 한다.
퍼셉트론과 마찬가지로 (입력층에 속하지 않은) 각 뉴런에는 각 weight와 bias가 할당된다.
'''


def sigmoid(t):
	return 1 / (1 + math.exp(-t))


'''
단순한 step_function 대신 sigmoid를 사용하는 이유는 신경망을 사용하기 위해 미적분을 사용할 것이고,
미적분을 사용하기 위해서는 부드러운 (smooth) 모양을 가진 함수를 사용해야 하기 때문
step_function은 연속적인 값을 가지지 않지만, sigmoid는 그것을 잘 근사한 부드러운 곡선이다.
sigmoid : 함수의 모양을 지칭
logistic : 함수 자체를 지칭
'''


def neuron_output(weights, inputs):
	return sigmoid(dot(weights, inputs))


def feed_forward(neural_network, input_vector):
	"""
	((층의) list의 (뉴런의) list 의 (weight)의 list)으로
	구성된 신경망을 입력받고
	순방향으로 전달하여 결과를 반환
	"""

	outputs = []

	# 한 층별로 계산
	for layer in neural_network:
		input_with_bias = input_vector + [1]  # bias를 추가
		output = [neuron_output(neuron, input_with_bias)  # 각 뉴런의 결과값
				  for neuron in layer]  # 계산
		outputs.append(output)  # 그리고 저장

		# 그리고 이번 층의 결과가 다음 층의 입력 변수가 된다
		input_vector = output

	return outputs


xor_network = [
	# hidden layer
	[[20, 20, -30],  # 'and' 뉴런
	 [20, 20, -10]],  # 'or' 뉴런
	# output layer
	[[-60, 60, -30]]  # 1번째 입력 값이 아닌 2번째 입력값을 받는 뉴런
]

for x in [0, 1]:
	for y in [0, 1]:
		# 순방향 신경망은 모든 뉴런에서 결과를 계산
		# feed_forward[-1]은 출력층의 결과
		print(x, y, feed_forward(xor_network, [x, y])[-1])

'''
Backpropagation
흔히 사용하는 방법으로는 backpropagation(역전파)이 있다.
backpropagation 은 경사하강법과 유사점이 상당히 많다
'''


def backpropagate(network, input_vector, target):
	hidden_outputs, outputs = feed_forward(network, input_vector)

	# output * (1 - output)은 sigmoid의 미분임
	output_deltas = [output * (1 - output) * (output - target[i])
					 for i, output in enumerate(outputs)]

	# 출력층의 뉴런마다 weight를 조정
	for i, output_neuron in enumerate(network[-1]):
		# i번째 출력층의 뉴런에 대해
		for j, hidden_output in enumerate(hidden_outputs + [1]):
			# 이 뉴런의 변화량과 j번째 입력 값을 고려하여
			# j번째 weight를 조정
			output_neuron[j] -= output_deltas[i] * hidden_output

	# 은닉층으로 오류값을 뒤로 전파
	hidden_deltas = [hidden_output * (1 - hidden_output) *
					 dot(output_deltas, [n[i] for n in network[-1]])
					 for i, hidden_output in enumerate(hidden_outputs)]

	# 은닉층의 뉴런마다 weight를 조정
	for i, hidden_neuron in enumerate(network[0]):
		for j, input in enumerate(input_vector + [1]):
			hidden_neuron[j] -= hidden_deltas[i] * input


'''
신경망과 각 이미지에 해당하는 숫자를 맞추는 것이 목적이기 때문에 10개의 입력값에 대한 출력값을 만들어야 한다.
예를 들어, 숫자 4에 대한 출력값은 다음과 같이 만들면 된다

[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
이런 형태를 one-of-k 벡터라고 하거나 one-hot encoding 이 되었다고 한다.
'''

# 입력값이 숫자 0부터 9까지이미로, 모든 출력값은 다음과 같이 나타낼 수 있다.
target = [[1 if i == j else 0 for i in range(10)]
		  for j in range(10)]
print(target)

raw_digits = [
	"""11111
	   1...1
	   1...1
	   1...1
	   11111""",

	"""..1..
	   ..1..
	   ..1..
	   ..1..
	   ..1..""",

	"""11111
	   ....1
	   11111
	   1....
	   11111""",

	"""11111
	   ....1
	   11111
	   ....1
	   11111""",

	"""1...1
	   1...1
	   11111
	   ....1
	   ....1""",

	"""11111
	   1....
	   11111
	   ....1
	   11111""",

	"""11111
	   1....
	   11111
	   1...1
	   11111""",

	"""11111
	   ....1
	   ....1
	   ....1
	   ....1""",

	"""11111
	   1...1
	   11111
	   1...1
	   11111""",

	"""11111
	   1...1
	   11111
	   ....1
	   11111"""]


def make_digit(raw_digit):
	return [1 if c == '1' else 0
			for row in raw_digit.split("\n")
			for c in row.strip()]


inputs = list(map(make_digit, raw_digits))

targets = [[1 if i == j else 0 for i in range(10)]
		   for j in range(10)]

random.seed(0)  # 매번 동일한 결과를 얻기 위해서
input_size = 25  # 입력 변수는 길이가 25인 벡터
num_hidden = 5  # 은닉층은 5개의 뉴런으로 구성
output_size = 10  # 각 입력 변수의 결과값은 길이가 10인 벡터

# 은닉층의 각 뉴런은 각 입력 값에 대한 weight와 bias를 갖고 있다
hidden_layer = [[random.random() for __ in range(input_size + 1)]
				for __ in range(num_hidden)]

# 출력층의 각 뉴런은 각 은닉층의 뉴런에 대한 weight와 bias를 갖고 있다
output_layer = [[random.random() for __ in range(num_hidden + 1)]
				for __ in range(output_size)]

# 이 신경망은 초기에 임의의 weight로 시작
network = [hidden_layer, output_layer]

'''
이제 backpropagation 알고리즘을 이용해 학습
'''
# 10000번 반복하면 충분히 수렴할 것이다
for __ in range(10000):
	for input_vector, target_vector in zip(inputs, targets):
		backpropagate(network, input_vector, target_vector)


def predict(input):
	return feed_forward(network, input)[-1]


for i, input in enumerate(inputs):
	outputs = predict(input)
	print(i, [round(p, 2) for p in outputs])