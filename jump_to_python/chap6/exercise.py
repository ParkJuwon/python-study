# 문자열 압축하기
## Q1
def compress_string(str_list):
	before_str = None
	count = 1
	result = ""
	for s in list(str_list):
		print(before_str, s)
		if(before_str != s):
			if(before_str):
				result += before_str + str(count)
				count = 1
			before_str = s
		else:
			count = count + 1

	return result + before_str + str(count)


print(compress_string("aaabbcccccca"))


# Duplicate Numbers
## Q1
print(list(range(0,10)))
a = list(range(0,10))
b = [0,1,2,3,4,5,6,7,8,9]
c = [9,1,2,3,4,5,6,7,8,0]
print(a == b)
print(a == c)
def duplicate_number(inputdata):
	splitdata = str(inputdata).split(" ")

	result = ""
	check_list = list(range(0, 10))
	for data in splitdata:
		sorted_list = sorted(list(data))
		sorted_list = list(map(lambda x: int(x), sorted_list))

		if check_list == sorted_list:
			result += "true "
		else:
			result += "false "
	return result

inputdata = "0123456789 01234 01234567890 6789012345 012322456789"
print(duplicate_number(inputdata))

# 모스 부호 해독
## Q1
dic = {
	".-": "A",
	"-...": "B",
	"-.-.": "C",
	"-..": "D",
	".": "E",
	"..-.": "F",
	"--.": "G",
	"....": "H",
	"..": "I",
	".---": "J",
	"-.-": "K",
	".-..": "L",
	"--": "M",
	"-.": "N",
	"---": "O",
	".--.": "P",
	"--.-": "Q",
	".-.": "R",
	"...": "S",
	"-": "T",
	"..-": "U",
	"...-": "V",
	".--": "W",
	"-..-": "X",
	"-.--": "Y",
	"--..": "Z"
}

def morse(value):

	verbs = value.split("  ")
	result = ""
	for verb in verbs:
		alphas = verb.split(" ")

		for alpha in alphas:
			result += dic[alpha]

		result += " "

	return result

morse_string = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
print(morse(morse_string))