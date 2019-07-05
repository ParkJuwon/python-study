import threading
import time

def say(msg):
	while True:
		time.sleep(1)
		print(msg)

for msg in ["you", "need", "python"]:
	t = threading.Thread(target=say, args=(msg,))
	t.daemon = True # 프로그램이 종료하면 데몬 쓰레드도 종료
	t.start()

for i in range(100):
	time.sleep(0.1)
	print(i)

