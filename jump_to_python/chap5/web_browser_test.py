import webbrowser

if __name__ == "__main__":
	webbrowser.open("http://google.com") # 이미 실행 상태이면 입력 주소로 이동

	# 항상 새로운 창으로
	webbrowser.open_new("http://google.com")
