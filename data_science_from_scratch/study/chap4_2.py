# -*- coding: utf-8 -*-

def make_matrix(num_rows, num_cols, entry_fn):
    """(i,j) 번째 원소가 entry_fn(i,j)인
    num_rows x num_cols list 반환"""
    return [[entry_fn(i, j)
    for j in range(num_cols)]
    for i in range(num_rows)]

def is_diagonal(i, j):
    """대각선의 원소는1, 나머지 원소는 0"""
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
print identity_matrix