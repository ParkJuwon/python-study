from stats import mean, corr, stdev
import random


# yi = beta * xi + alpha + ei
# yi : 사용자 i 가 매일 사이트에서 보내는 시간(분)
# xi : 사용자 i의 친구 수
# ei : 모델이 고려하지 못하는 다른 요소 때문에 발생하는 작은 오류

def predict(alpha, beta, x_i):
	return beta * x_i + alpha


def error(alpha, beta, x_i, y_i):
	"""실제 결과가 y_i 일 때,
	beta * x_i + alpha로 계산된 예측값의 오류"""
	return y_i - predict(alpha, beta, x_i)


def sum_of_squared_errors(alpha, beta, x, y):
	return sum(error(alpha, beta, x_i, y_i) ** 2
			   for x_i, y_i in zip(x, y))


# 최소 자승법이란 sum_of_squared_errors를 최소화해 주는 알파와 베타 값을 찾는것을 의미.
# 미분을 사용하면 오류를 최소화하는 알파와 베타를 찾을 수 있다.

def least_squares_fit(x, y):
	"""x와 y가 학습 데이터로 주어졌을 때
	오류의 제곱 값을 최소화해 주는 알파와 베타를 계산"""
	beta = corr(x, y) * stdev(y) / stdev(x)
	alpha = mean(y) - beta * mean(x)
	return alpha, beta


# 결정계수란 종속 변수의 총 변화량 중 모델이 잡아낼 수 있는 변화량의 비율

def de_mean(x):
	"""x의 모든 데이터 포인트에서 평균을 뺌"""
	n = len(x)
	x_bar = sum(x) / n
	return [x_i - x_bar for x_i in x]


def total_sum_of_squares(y):
	"""평균을 기준으로 y_i의 변화량을 제곱한 값의 총합"""
	return sum(v ** 2 for v in de_mean(y))


def r_squared(alpha, beta, x, y):
	"""모델이 잡아낼 수 있는 변화량의 비율은
	1 - 모델이 잡아내지 못하는 변화량의 비율로 계산할 수 있다"""
	return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y))


# 최소자승법 모델의 성능은 적어도 평균을 예측하는 모델의 성능만큼 좋아야 한다.
# 즉, 오류를 제곱한 값의 총합은 아무리 커봐야 변화량을 제곱한 값의 총합과 동일
# 그리고 오류를 제곱한 값의 총합은 최소한 0 이기 때문에 R 제곱 값의 최대값은 1이다.
# R제곱값이 클수록 모델이 데이터에 더 적합하다는 것을 의미.


def in_random_order(data):
	"""generator that returns the elements of data in random order"""
	indexes = [i for i, _ in enumerate(data)]  # create a list of indexes
	random.shuffle(indexes)  # shuffle them
	for i in indexes:  # return the data in that order
		yield data[i]


def vector_subtract(v, w):
	"""subtracts two vectors componentwise"""
	return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c, v):
	return [c * v_i for v_i in v]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
	data = list(zip(x, y))
	theta = theta_0  # initial guess
	alpha = alpha_0  # initial step size
	min_theta, min_value = None, float("inf")  # the minimum so far
	iterations_with_no_improvement = 0

	# if we ever go 100 iterations with no improvement, stop
	while iterations_with_no_improvement < 100:
		value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

		if value < min_value:
			# if we've found a new minimum, remember it
			# and go back to the original step size
			min_theta, min_value = theta, value
			iterations_with_no_improvement = 0
			alpha = alpha_0
		else:
			# otherwise we're not improving, so try shrinking the step size
			iterations_with_no_improvement += 1
			alpha *= 0.9

		# and take a gradient step for each of the data points
		for x_i, y_i in in_random_order(data):
			gradient_i = gradient_fn(x_i, y_i, theta)
			theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

	return min_theta

def squared_error(x_i, y_i, theta):
	alpha, beta = theta
	return error(alpha, beta, x_i, y_i) ** 2


def squared_error_gradient(x_i, y_i, theta):
	alpha, beta = theta
	return [-2 * error(alpha, beta, x_i, y_i),  # 알파에 대한 편미분
			-2 * error(alpha, beta, x_i, y_i) * x_i]  # 베타에 대한 편미분


if __name__ == "__main__":
	num_friends_good = [49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11,
						10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
						9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
						7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5,
						5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3,
						3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
						2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	daily_minutes_good = [68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, 54.01, 38.79, 47.59,
						  49.1, 27.66, 41.03, 36.73, 48.65, 28.12, 46.62, 35.57, 32.98, 35, 26.07, 23.77, 39.73, 40.57,
						  31.65, 31.21, 36.32, 20.45, 21.93, 26.02, 27.34, 23.49, 46.94, 30.5, 33.8, 24.23, 21.4, 27.94,
						  32.24, 40.57, 25.07, 19.42, 22.39, 18.42, 46.96, 23.72, 26.41, 26.97, 36.76, 40.32, 35.02,
						  29.47, 30.2, 31, 38.11, 38.18, 36.31, 21.03, 30.86, 36.07, 28.66, 29.08, 37.28, 15.28, 24.17,
						  22.31, 30.17, 25.53, 19.85, 35.37, 44.6, 17.23, 13.47, 26.33, 35.02, 32.09, 24.81, 19.33,
						  28.77, 24.26, 31.98, 25.73, 24.86, 16.28, 34.51, 15.23, 39.72, 40.8, 26.06, 35.76, 34.76,
						  16.13, 44.04, 18.03, 19.65, 32.62, 35.59, 39.43, 14.18, 35.24, 40.13, 41.82, 35.45, 36.07,
						  43.67, 24.61, 20.9, 21.9, 18.79, 27.61, 27.21, 26.61, 29.77, 20.59, 27.53, 13.82, 33.2, 25,
						  33.1, 36.65, 18.63, 14.87, 22.2, 36.81, 25.53, 24.62, 26.25, 18.21, 28.08, 19.42, 29.79, 32.8,
						  35.99, 28.32, 27.79, 35.88, 29.06, 36.28, 14.1, 36.63, 37.49, 26.9, 18.58, 38.48, 24.48,
						  18.95, 33.55, 14.24, 29.04, 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9, 27.2, 32.01, 29.27,
						  33, 13.74, 20.42, 27.32, 18.23, 35.35, 28.48, 9.08, 24.62, 20.12, 35.26, 19.92, 31.02, 16.49,
						  12.16, 30.7, 31.22, 34.65, 13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12, 24.42, 9.82,
						  23.39, 30.93, 15.03, 21.67, 31.09, 33.29, 22.61, 26.89, 23.48, 8.38, 27.81, 32.35, 23.84]

	alpha, beta = least_squares_fit(num_friends_good, daily_minutes_good)

	print("alpha", alpha)
	print("beta", beta)

	print("r-squared", r_squared(alpha, beta, num_friends_good, daily_minutes_good))

	# 경사 하강법 사용
	# 만약 theta = [alpha, beta] 로 설정하면 경사하강법을 통해 모델을 만들 수 있다.

	# 임의의 알파와 베타 값으로 시작
	random.seed(0)
	theta = [random.random(), random.random()]
	alpha, beta = minimize_stochastic(squared_error,
									  squared_error_gradient,
									  num_friends_good,
									  daily_minutes_good,
									  theta,
									  0.0001)

	print("alpha", alpha)
	print("beta", beta)
