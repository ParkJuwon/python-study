# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from collections import defaultdict, Counter

# 히스토그램(histogram) : 정해진 구간에 해당되는 항목의 개수를 보여줌으로써 값의 분포를 관찰할 수 있음
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10*10
histogram = Counter(decile(grade) for grade in grades)

plt.bar( [x - 4 for x in histogram.keys()], # 각 막대를 왼쪽으로 4만큼 옮기고
        histogram.values(), # 각 막대의 높이를 정해주고
        8 # 너비는 8
) 
plt.axis([-5, 105, 0 ,5])   # x축은 -5 부터 105
                            # y 축은 0부터 5
plt.xticks([10 * i for i in range(11)]) # x 축의 레이블은 0, 10, .... 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
# plt.show()


# axis 를 사용할 때는 신중해야한다 y축이 0에서 시작하지 않으면 오해를 불러 일으킴
mentions = [500,505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

plt.ticklabel_format(useOffset = False)

plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Look at the 'Huge' Increase! ")
# plt.show()

plt.axis([2012.5 ,2014.5 ,0 ,550])
plt.title("Not so Huge Anymore")
plt.show()