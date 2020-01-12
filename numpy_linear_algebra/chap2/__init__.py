import numpy as np

# 넘파이 배열 원소는 모두 같은 데이터 타입

A = np.array([1, 2, 3])

# 차원 개수 만큼 정수로 인덱싱 된다.
# 차원을 축(axis)	이라고 도 부른다

a = np.array([0.1, 0.2, 0.3])
print(a)

# numpy 실수 데이터 저장시 디폴트 데이터 타입은 float64
print(a.dtype)

# 넘파이의 64비트 실수 타입
print(type(a[0]))

b = np.array([1, 2, 3])
print(b.dtype)

print(type(b[0]))

# 넘파이에서 특징 적으로 complex64 / complex128 가 있음
# complex64 : 복소수 32비트 실수 2개로 실수와 허수를 나타냄
# complex128 : 복소수 64비트 실수 2개로 실수와 허수를 나타냄

c = np.array([1, 2, 3], dtype=np.float64)
print(c)

print(c.dtype)

# 다입 변경
d = np.array([1.1, 2.2, 3.3, 4.9])
print(d.dtype)
e = d.astype(np.int32)
print(e)

A = np.array([[1, 2, 3], [4, 5, 6]])
print(type(A))
print(A.ndim)  # 차원의 개수
print(A.shape)
print(A.size)  # 전체 길이
print(A.dtype)
print(A.itemsize)  # 바이트
print(A.data)  # 저장되어 있는 버퍼

b = np.array([1, 2, 3, 4, 5, 6])
print(b.max())
print(b.min())
print(b.sum())
print(b.mean())

c = np.array([[1, 2], [3, 4]])
print(c)
print(c.sum(axis=0))  # 열방향
print(c.sum(axis=1))  # 행방향

### np print 생략 없이 전체 배열을 출력 하려면
import sys

np.set_printoptions(threshold=sys.maxsize)

# numpy 배열의 경우 대응 하는 원소벼로 연산을 하는 벡터라이제이션을 지원하기 때문에 스칼라 계산을 하듯 연산 할수 있다.
A = np.array([1, 2, 3])
B = np.array([3, 5, 2])
print(A + B)

# 배열 생성 함수
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.empty((5, 5)))
print(np.random.random((3, 3)))

# 연속 원소 배열 생성 함수
print(np.arange(0, 50, 5))
print(np.arange(0.1, 2.5))  # 1 간격으로 뽑아서 배열
print(np.arange(10))

# linspace 함수는 지정한 범위 내에 원하는 원소개로 숫자를 뽑아서 배열을 생성
print(np.linspace(0, 10, 10))
print(np.linspace(0, 100))  # 디폴트 50

A = np.array([[1, 2], [3, 4]])
print(A.shape)
print(A.ravel())  # 1차원 배열로 변환해서 리턴

A = np.arange(12)
print(A)
print(A.resize(3, 4))  # 뷰를 생성하지 않고 배열의 shape 를 바꿈
print(A)

a = np.array([1, 2, 3])
a = a[:, np.newaxis]  # 차원을 증가시켜줌
print(a.shape)  # 열백터
print(a)

b = np.array([4, 5, 6])
b = b[np.newaxis, :]
print(b.shape)
print(b)  # 행백터

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 0], [0, 1]])
C = np.vstack((A, B))  # 열 방향 결합
print(C)
D = np.hstack((A, B))  # 행 방향 결합
print(D)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
E = np.column_stack((a, b, c))  # 1차원을 배열을 열백터로 하는 2차원 배열을 만듬
print(E)

# concatenate 함수는 지정한 차원 방향으로 배열을 결합
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 0], [0, 1]])
print(np.concatenate((A, B), axis=0))  # 열방향
print(np.concatenate((A, B), axis=1))  # 행방향

# 배열 분할
A = np.arange(9).reshape(3, 3)
a = np.hsplit(A, 3)  # 배열을 행 방향으로 3개로 분할
print(A)
print(a)

B = np.arange(18).reshape(3, 6)
print(B)
# 지정한 범위를 기준으로 다음과 같이 3개로 분할
# B[:,0:2], B[:,2:5], B[:,5:]
b = np.hsplit(B, (2, 5))
print(b)

A = np.arange(9).reshape(3, 3)
# vsplit은 열방향으로 분할
a = np.vsplit(A, 3)
print(A)
print(a)

# T는 행과 열을 교환하여 얻게되는 전치행렬
A = np.arange(9).reshape(3, 3)
print(A)
print(A.T)  # 전치행렬
print(A.flat)  # 개별 출력

# 배열 접근 표현
print(A[1, 2])
print(A[1][2])

# 행 슬라이싱
print(A[0])
print(A[0, :])

# 열 슬라이싱
print(A[:, 0])

# 하나이상의 인덱스를 생략 시 ... 를 사용가능
print(A[..., 0])  # 첫 번째 열을 슬라이싱 합니다.
print(A[..., 1])  # 두번째 열을 슬라이싱

# 얕은 복사
a = np.arange(12)
b = a.view()
print(b.base is a)

# 깊은 복사
a = np.arange(12)
b = a.copy()
print(b.base is a)

A = np.array([2, 4, 6, 8]).reshape(2, 2)
B = np.array([2, 2, 2, 2]).reshape(2, 2)

print(A + B)  # 원소간 덧셈
print(A - B)  # 원소간 뺄셈
print(A * B)  # 원소간 곱셈
print(np.dot(A, B))  # 내적
print(A @ B)  # 내적 (3.5 이상)
print(A / B)  # 원소간 나눗셈


