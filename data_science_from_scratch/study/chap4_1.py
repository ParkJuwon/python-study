# -*- coding: utf-8 -*-

def vector_add(v, w):
    """각 성분끼리 더한다 """
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """각 성분끼리 뺀다 """
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """모든 벡터의 각 성분들끼리 더한다"""
    result = vectors[0]                     # 첫 번째 벡터부터 시작해서
    for vector in vectors[1:]:              # 나머지 벡터들을
        result = vector_add(result, vector) # 더해준다

def vector_sum(vectors):
    return reduce(vector_add, vectors)

from functools import partial
vector_sum = partial(reduce, vector_add)

# 벡터에 스칼라를 곱해줄수 있어야 함
def scala_multiply(c, v):
    """c 는 숫자 v는 벡터"""
    return [c * v_i for v_i in v]

# 같은 길이의 벡터로 구성된 list가 주어졌을 떄 각 성분별 평균을 구할 수도 있다
def vector_mean(vectors):
    """i 번째 성분이 입력된 벡터의 i번째 성분의 평균을 의미하는 벡터를 계산해 준다"""
    n = len(vectors)
    return scala_multiply(1/n, vector_sum(vectors))

