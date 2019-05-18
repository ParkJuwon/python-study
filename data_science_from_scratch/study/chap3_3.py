# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from collections import defaultdict, Counter

variance=[1,2,4,8,16,32,64,128,256]
bias_squared= [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x,y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# 한 차트에 여러개의 series를 그리기 위해
# plt.plot을 여러번 호출
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error , 'b:', label='total error')

# 각 series에 label을 미리 달아 놨기 때문에
# 범례 (legend) 를 어렵지 않게 그릴수 있다
# 여기서 loc=9는 "top center(위쪽중앙)" 을 의미한다
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()