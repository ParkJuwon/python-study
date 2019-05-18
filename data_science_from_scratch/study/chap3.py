# -*- coding: utf-8 -*-

# 시각화의 두가지 목적
# 데이터 탐색
# 데이터 전달

# matplotlib
# 웹을 위한 복잡하고 인터렉티브한 시각화를 위해 좋은 선택은 아니지만
# 단단한 막대 그래프, 선그래프, 또는 산점도 그릴때는 나쁘지 않다
# matplotlib.pyplot 모듈 사용
# pyplot은 시각화를 단계별로 간단하게 만들 수 있는 구조로 되어 있으며,
# 시각화가 완성되면 savefig()를 통해 그래프를 저장하거나 show() 를 사용하여 화면에 띄울수 있다

from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# x축에 연도, y 축에 GDP가 있는 선 그래프를 만들자
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# 제목을 더하자
plt.title("Nominal GDP")
# y축에 레이블을 추가하자
plt.ylabel("Billions of $")
plt.show()

