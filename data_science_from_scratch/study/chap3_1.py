# -*- coding: utf-8 -*-

# 막대 그래프
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 막대 너비의 기본값이 0.8
# 막대가 가운데로 올 수 있도록 왼쪽 좌표에 0.1씩 더해줌
xs = [i + 0.1 for i, _ in enumerate(movies)]

# 왼편으로부터 x 축의 위치기ㅏ xs이고 높이가 num_oscars 인 막대를 그리자
from matplotlib import pyplot as plt
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# 막대의 가운데에 오도록 영화 제목 레이블을 달자
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()