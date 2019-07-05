import threading
import time

class MyThread(threading.Thread):
	def __init__(self, msg):
		threading.Thread.__init__(self) # 부모클래스의 생성자를 반드시 호출 해줘야 한다.
		self.msg = msg
		self.daemon = True

	def run(self):
		while True:
			time.sleep(1)
			print(self.msg)

for msg in ["you", "need", "python"]:
	t = MyThread(msg)
	t.start() # thread의 start호출시 run() 이 실행됨

for i in range(100):
	time.sleep(0.1)
	print(i)