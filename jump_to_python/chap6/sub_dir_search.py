import os

def search(dirname):
	filenames = os.listdir(dirname)
	for filename in filenames:
		full_filename = os.path.join(dirname, filename)
		ext = os.path.splitext(full_filename)[-1] # splitext: 확장자를 기준으로 나누어줌

		if ext == ".py":
			print(full_filename)

search("/Users/user/develop/python-study/jump_to_python/chap5")
