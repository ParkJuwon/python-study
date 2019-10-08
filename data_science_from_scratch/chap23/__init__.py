from collections import defaultdict

'''
데이터 베이스는 데이터를 효과적으로 저장하고 질의, 또는 쿼리(query) 하기 위한 시스템이고
이중 대부분은 Oracle, MySql, SQL server 등과 같이 데이터를 테이블에 저장하고 SQL(structured query language)로
쿼리하는 관계형 데이터베이스(relational database)이다.

SQL은 선언적 언어의 일종으로, 데이터 과학자에게는 필수적인 도구 중 하나이다.
NotQuiteABase라는 파이썬 구현체를 만들어서 SQL을 실제로 적용해 보고 데이터베이스가 어떻게 동작하는지 살펴봄
'''

'''
CREATE TABLE과 INSERT
테이블에는 열의 이름과 데이터 타입(data type)이 명시된 스키마(schema)가 추가된다.
'''

users = [[0, "Hero", 0],
		 [1, "Dunn", 2],
		 [2, "Sue", 3],
		 [3, "Chi", 3]]

'''
SQL 에서는 이 테이블을 다음과 같이 생성
CREATE TABLE users(
	user_id INT NOT NULL,
	name VARCHAR(200),
	num_friends INT
);

데이터 행은 INSERT 문으로 입력할 수 있다.
INSERT INTO users(user_id, name, num_friends) VALUES (0, 'Hero', 0);

SQL문은 항상 세미콜론(;)으로 끝난다. 또한 문자열을 입력할 때는 작은 따옴표 (')를 쓴다.
'''


class Table:
	def __init__(self, columns):
		self.columns = columns
		self.rows = []

	def __repr__(self):
		"""Table을 이쁘게 표현하기 위해 열 다음 행을 출력"""
		return str(self.columns) + "\n" + "\n".join(map(str, self.rows))

	def insert(self, row_values):
		if len(row_values) != len(self.columns):
			raise TypeError("wrong number of elements")
		row_dict = dict(zip(self.columns, row_values))
		self.rows.append(row_dict)

	def update(self, updates, predicate):
		for row in self.rows:
			if predicate(row):
				for column, new_value in updates.items():
					row[column] = new_value

	def delete(self, predicate=lambda row: True):
		""""predicate 에 해당하는 모든 행을 제거
		만약 predicate가 주어지지 않았다면 모든 행을 제거"""
		self.rows = [row for row in self.rows if not (predicate(row))]

	def select(self, keep_columns=None, additional_columns=None):

		if keep_columns is None:  # 만약 특정 열이 명시되지 않았다면
			keep_columns = self.columns  # 모든 열 반환

		if additional_columns is None:
			additional_columns = {}

		# 결과를 저장하기 위한 새로운 Table
		result_table = Table(keep_columns + list(additional_columns.keys()))

		for row in self.rows:
			new_row = [row[column] for column in keep_columns]
			for column_name, calculation in additional_columns.items():
				new_row.append(calculation(row))
			result_table.insert(new_row)

		return result_table

	def where(self, predicate=lambda row: True):
		"""주어진 predicate 에 해당하는 행만 반환"""
		where_table = Table(self.columns)
		where_table.rows = list(filter(predicate, self.rows))
		return where_table

	def limit(self, num_rows=None):
		"""첫 num_rows 만큼의 행만 반환"""
		limit_table = Table(self.columns)
		limit_table.rows = (self.rows[:num_rows]
							if num_rows is not None
							else self.rows)
		return limit_table

	def group_by(self, group_by_columns, aggregates, having=None):

		grouped_rows = defaultdict(list)

		# grouped_row를 채우기
		for row in self.rows:
			key = tuple(row[column] for column in group_by_columns)
			grouped_rows[key].append(row)

		# 열이 group_by_columns을 나타내고 행이 aggregates 를 나타내는 table을 생성
		result_table = Table(group_by_columns + list(aggregates.keys()))

		for key, rows in grouped_rows.items():
			if having is None or having(rows):
				new_row = list(key)
				for aggregate_name, aggregate_fn in aggregates.items():
					new_row.append(aggregate_fn(rows))
				result_table.insert(new_row)

		return result_table

	def order_by(self, order):
		new_table = self.select()  # 기존 Table을 복사
		new_table.rows.sort(key=order)
		return new_table

	def join(self, other_table, left_join=False):

		join_on_columns = [c for c in self.columns  # 양쪽 테이블이
						   if c in other_table.columns]  # 모두 포함하는 열

		additional_columns = [c for c in other_table.columns  # 오른쪽 테이블에만
							  if c not in join_on_columns]  # 존재하는

		# 왼쪽 테이블의 모든 열 + 오른쪽 테이블의 추가적인 열
		join_table = Table(self.columns + additional_columns)

		for row in self.rows:
			def is_join(other_row):
				return all(other_row[c] == row[c] for c in join_on_columns)

			other_rows = other_table.where(is_join).rows

			# 반환되는 테이블의 각 행을 현재 행과 일치하는 other_row로 구성
			for other_row in other_rows:
				join_table.insert([row[c] for c in self.columns] +
								  [other_row[c] for c in additional_columns])

			# 만약 일치하는 행이 없다면, left join을 의미하며 None을 포함하는 테이블을 반환
			if left_join and not other_rows:
				join_table.insert([row[c] for c in self.columns] +
								  [None for c in additional_columns])

		return join_table


# 예를 들면 다음과 같은 작업을 할 수 있다.
users = Table(["user_id", "name", "num_friends"])
users.insert([0, "Hero", 0])
users.insert([1, "Dunn", 2])
users.insert([2, "Sue", 3])
users.insert([3, "Chi", 3])
users.insert([4, "Thor", 3])
users.insert([5, "Clive", 2])
users.insert([6, "Hicks", 3])
users.insert([7, "Devin", 2])
users.insert([8, "Kate", 2])
users.insert([9, "Klein", 3])
users.insert([10, "Jen", 1])

print(users)

'''
UPDATE

Dunn 에게 친구가 한명 더 생겼다고 하면 SQL로 다음과 같은 쿼리를 던질 것이다.

UPDATE users
SET num_friends = 3
WHERE user_id = 1;

이때 명시해야 하는 것은 다음과 같다
	어떤 테이블을 업데이트할 것인가
	어떤 행을 업데이트할 것인가
	어떤 열을 업데이트할 것인가
	어떤 값으로 치환할 것인가
'''

users.update({'num_friends': 3},  # num_friends = 3 으로 설정
			 lambda row: row['user_id'] == 1)  # user_id == 1 인 행에서
print(users.rows[1])

'''
DELETE

SQL 로 행을 지우는 방법은 두가지가 있다. 모든 행을 지우는 일, 특정 조건(condition)을 만족하는 행만 지우는 일
DELETE FROM users;
DELETE FROM users WHERE user_id = 1;
'''
# users.delete(lambda row: row["user_id"] == 1) # user_id == 1 인 행 제거
# print(users)
# users.delete() # 모든 행 제거
# print(users)

'''
SELECT
몇가지 행만 선택해서 보는 경우가 많다.

SELECT * FROM users;							- 모든 내용을 선택
SELECT * FROM users LIMIT 2;					- 첫 두 행만 선택
SELECT user_id FROM users;						- 특정 열만 선택
SELECT user_id FROM users WHERE name = 'Dunn';	- 특정 행만 선택

SELECT 문은 필드값을 계산하기 위해 사용하기도 한다
SELECT LENGTH(name) AS name_length FROM users;

SELECT 함수 추가, 두개의 선택적 인자를 전달 받음
	- keep_columns 에는 보존하고 싶은 열의 이름 입력, 명시하지 않으면 모든열 보존
	- additional_column 에는 새로 추가하고 싶은 열을 dict 형태로 입력. 이때 dict 키는 추가 되는 열의 이름, 값은 계산하는 방법
	- 두 인자 중 아무것도 전달하지 않으면 입력한 테이블과 같은 테이블 그대로 반환
'''

'''
추가로 where(), limit() 함수도 추가
'''

# SELECT * FROM users;
print(users.select())
print()

# SELECT * FROM users LIMIT 2;
print(users.limit(2))
print()

# SELECT user_id FROM users;
print(users.select(keep_columns=['user_id']))
print()

# SELECT user_id FROM users WHERE name = 'Dunn';
print(users.where(lambda row: row['name'] == 'Dunn').select(keep_columns=['user_id']))
print()


# SELECT LENGTH(name) AS name_length FROM users;
def name_length(row): return len(row['name'])

print(users.select(keep_columns=[], additional_columns={'name_length': name_length}))
print()

'''
GROUP BY
지정된 열에서 동일한 값을 가진 행을 묶어주며, MIN, MAX, COUNT, SUM 등 의 병합 계산을 할수 있게 해준다.

예를 들어, 이름의 길이에 따른 사용자의 수와 가장 작은 user_id를 알고 싶을 수 있다.
SELECT LENGTH(name) as name_length,
	MIN(user_id) as min_user_id,
	COUNT(*) AS num_users
FROM users
GROUP BY LENGTH(name);

선택되는 모든 데이터 필드는 name_length 처럼 GROUP BY에 포함되어 있거나 
min_user_id, num_users 처럼 계산되는 테이블 전체에 포함되어 있어야 한다.

SQL 에는 WHERE 절과 유사한 HAVING 절도 있는데, 병합하기 전에 필터링 하는 WHERE 절과 달리 HAVING절은 병함된 결과를 필터링한다.

또는 이름이 특정 글자로 시작하는 사용자들의 평균 친구 수를 보고 싶을 수도 있다.
그중 친구수가 평균적으로 1 이상인 경우만 출력
SELECT SUBSTR(name, 1, 1) AS first_letter,
	AVG(num_friends) AS avg_num_friends
FROM users
GROUP BY SUBSTR(name, 1, 1)
HAVING AVG(num_friends) >1;

전체에 대한 총합을 구하고 싶을 때는 GROUP BY 부분만 제거하면 된다.
SELECT SUM(user_id) as user_id_sum
FROM users
WHERE user_id > 1;

GROUP BY 함수 추가, 그룹으로 묶고 싶은 열의 이름인 group_by_columns와 
각 그룹에 적용하고 싶은 병합 함수에 대한 dict인 aggregates,
여러 열에 적용되는 having 이라는 인자를 받아 다음과 같이 작동
	- 키가 group_by_columns의 항목이고 값이 해당 키에 대응되는 목록인 defaultdict 생성
	- 테이블의 행을 훑으며 defaultdict의 값을 채운다.
	- 새로운 테이블 생성
	- defaultdict 를 훑으며 having 필터를 적용하고, 새로운 테이블에 값을 채워 넣음
'''


# 앞서 작성한 SQL문과 동일한 코드 작성
def min_user_id(rows): return min(row['user_id'] for row in rows)


stats_by_length = users \
	.select(additional_columns={'name_length': name_length}) \
	.group_by(group_by_columns=['name_length'],
			  aggregates={'min_user_id': min_user_id,
						  'num_users': len})

print(stats_by_length)
print()


# first_letter
def first_letter_of_name(row):
	return row['name'][0] if row['name'] else ''


def average_num_friends(rows):
	return sum(row['num_friends'] for row in rows) / len(rows)


def enough_friends(rows):
	return average_num_friends(rows) > 1


avg_friends_by_letter = users \
	.select(additional_columns={'first_letter': first_letter_of_name}) \
	.group_by(group_by_columns=['first_letter'],
			  aggregates={'avg_num_friends': average_num_friends},
			  having=enough_friends)

print(avg_friends_by_letter)
print()


# user_id_sum
def sum_user_ids(rows): return sum(row['user_id'] for row in rows)


user_id_sum = users \
	.where(lambda row: row['user_id'] > 1) \
	.group_by(group_by_columns=[],
			  aggregates={'user_id_sum': sum_user_ids})

print(user_id_sum)
print()

'''
ORDER BY
결과값을 정렬하고 싶을 때

SELECT * FROM users
ORDER BY name
LIMIT 2;
'''
friendliest_letter = avg_friends_by_letter \
	.order_by(lambda row: -row['avg_num_friends']) \
	.limit(4)
print(friendliest_letter)
print()

'''
JOIN
관계형 데이터베이스는 종종 중복을 최소화하도록 정규화(normalize) 되어 있다.

user_interests를 생성해서 user_ids와 관심사 사이에 1:N 관계를 성립하게 함
CREATE TABLE user_interests (
	user_id INT NOT NULL,
	interest VARCHAR(100) NOT NULL
);
'''
user_interests = Table(["user_id", "interest"])
user_interests.insert([0, "SQL"])
user_interests.insert([0, "NoSQL"])
user_interests.insert([2, "SQL"])
user_interests.insert([2, "MySQL"])

'''
SQL 에 관심있는 사용자 목록을 얻고 싶을 때
SELECT users.name
FROM users
JOIN user_interests
ON users.user_id = user_interests.user_id
WHERE user_interests.interest = 'SQL'

INNER JOIN 은 매칭 조건에 맞는 조합(만) 반환한다
한편 LEFT JOIN이라는 방식은 매칭 조건에 맞는 조합 뿐 아니라 매칭되지 않는 왼쪽 테이블 행까지도 모두 반환한다 
(이 경우 오른쪽 테이블에 해당하는 값은 모두 NULL 이 된다.)

LEFT JOIN을 사용하면 각 사용자의 관심사를 세는 것이 좀 더 쉬워진다
SELECT users.id, COUNT(user_interests.interest) AS num_interests
FROM users
LEFT JOIN user_interests
ON users.user_id = user_interests.user_id

LEFT JOIN은 병합된 데이터셋에서 관심사가 하나도 없는 사용자도 포함시켜 주며(user_interests에 NULL이 들어있음)
COUNT는 NULL이 아닌 값만 세어 준다.
'''

# SQL에 관심있는 사용자들
sql_users = users \
	.join(user_interests) \
	.where(lambda row: row['interest'] == 'SQL') \
	.select(keep_columns=['name'])

print(sql_users)
print()


# 관심사에 대한 수
def count_interests(rows):
	'''None이 아닌 관심사의 개수를 세어줌'''
	return len([row for row in rows if row['interest'] is not None])


user_interest_counts = users \
	.join(user_interests, left_join=True) \
	.group_by(group_by_columns=['user_id'],
			  aggregates={'num_interests': count_interests})

print(user_interest_counts)
print()

'''
한편 SQL에서는 매칭되지 않는 오른쪽 테이블의 행을 보존해 주는 RIGHT JOIN이 있고
양쪽 테이블 모두 매칭되지 않는 행을 보존해 주는 FULL OUTER JOIN도 있다.
'''

'''
서브쿼리

SQL에서는 쿼리의 결과물을 또 다른 테이블인 것처럼 간주하고 SELECT (또는 JOIN) 을 할 수 있다.
SELECT MIN(user_id) AS min_user_id FROM
(SELECT user_id FROM user_interests WHERE interest = 'SQL') sql_interests; 
'''
likes_sql_user_ids = user_interests \
	.where(lambda row: row['interest'] == 'SQL') \
	.select(keep_columns=['user_id'])

likes_sql_min_user_id = likes_sql_user_ids.group_by(group_by_columns=[],
													aggregates={'min_user_id': min_user_id})

print(likes_sql_min_user_id)
print()

'''
인덱싱
행을 훑을 때 행의 수가 아주 많다면 무척 오래 걸릴 것이다.
직접만든 join도 비효율적
또한 제약 조건을 주고 싶을 때도 있다. (user테이블에서 두 명 이상의 사람들이 같은 user_id를 갖지 못하게)
인덱싱(indexing) 은 이 모든것들을 해결해 줌
	전체를 훑어 보지않고 매칭
	유일성(unique) 조건이 있다면 중복된 값을 생성할 때 에러 발생   
'''

'''
쿼리 최적화
SQL에 관심있는 사용자 찾기
SELECT user.name
FROM users
JOIN user_interests
ON users.user_id = user_interests.user_id
WHERE user_interests.interest = 'SQL'
'''
# 쿼리를 쓰는 두가지 방법
# interests 테이블을 필터하고 join
join_result_first = user_interests \
	.where(lambda row: row['interest'] == 'SQL') \
	.join(users) \
	.select(['name'])

# join 후 필터
join_result_second = user_interests \
	.join(users) \
	.where(lambda row: row['interest'] == 'SQL') \
	.select(['name'])

print(join_result_first)
print(join_result_second)

# 효율성을 따지자면 더 적은 수의 행에 대해 join연산을 하는 방법이 좋음
# 보통은 쿼리엔진에서 최적화 해줌

'''
NoSql
최근 트랜드 중 하나는 데이터를 테이블로 표현하지 않는 비관계형(nonrelational) 데이터베이스 NoSql이다
MongoDB는 JSON 문서의 형태로 데이터를 표현
그 외에 행 대신 열에 데이터를 저장하는 컬럼형 데이터베이스도 있고 (이런 데이터베이스는 열의 수가 아주 많지만, 그중 일부만 쿼리에 사용할 때 좋다)
키로 복잡한 값을 반환하는 key-value 스토리지
그래프를위한 데이터베이스
여러 데이터 센터간 호환성을 고려한 데이터 베이스
메모리상에서 동작하는 데이터베이스
시계열 데이터를 저장하는 데이터베이스 등 

NoSQL은 '핫'하다
'''

'''
더 공부해 보고 싶다면
	- 관계형 데이터베이스를 간단히 사용해 보고 싶다면,SQLite는 아주 빠르고 작고, MySQL과 PostgreSQL은 조금 크지만 기능이 많다는 것을 참고
	- NoSQL을 탐색해 보고 싶다면 MongoDB가 좋은 출발점이 될 것이다.
	- NoSQL에 대한 위키피디아 페이지에는 이 책이 쓰여질 당시에는 존재하지도 않았던 다양한 데이터베이스의 종류를 나열해 주고 있다.
'''


