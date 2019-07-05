import re

data = """
park 800905-1049118
kim 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

"""
\d : 숫자와 매치 [0-9]
\D : 숫자가 아닌것과 매치 [^0-9]
\s : whitespace 
\S : whitespace 아닌것과 매치
\w : 문자 + 숫자 [a-zA-Z0-9]
\W : 문자 + 숫자 아닌것 [^a-zA-Z0-9]
"""

"""
match(): 문자열의 처음부터 정규식과 매치되는지 조사
search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사
findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴
finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복가능한 객체로 리턴
"""

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print(m)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)
for r in result: print(r)

"""
match
group(): 매치된 문자열 리턴
start(): 매치된 문자열의 시작 위치 리턴
end(): 매치된 문자열의 끝 위치 리턴
span(): 매치된 문자열의 (시작, 끝)에 해당되는 튜플 리턴
"""

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())


m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

p = re.compile("[a-z]+")
m = p.match("python")

m = re.match("[a-z]+", "python")

"""
컴파일 옵션
DOTALL (S) : 줄바꿈 문자를 포함해서 모든 문자가 매치
IGNORECASE (I) : 대소문 관계 없음
MULTILIN (M) : 여러줄과 매치 
VERBOSE (X) : verbose 모드 (정규식을 보기 편하게 만들수도 있고 주석등을 사용가능)
"""


p = re.compile("\\\\section")
p = re.compile(r"\\section")

"""
그룹핑된 문자열 재참조 : \1
"""
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

"""
그룹핑된 문자열에 이름 붙히기
(?P<name>\w+)
"""
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

# 재참조
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search("Paris in the the spring").group())

"""
전방 탐색
(?=...) 긍정형 전방 탐색 : ...에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소모되지 않는다
(?!...) 부정형 전방 탐색 : ...에 핻ㅇ되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소모되지 않는다
"""

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group()) # http:

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group()) # http

"""
확장자가 .bat 아닌 파일을 찾기
.*[.](?!bat$).*$

.bat, .exe 제거
.*[.](?!bat$|exe$).*$ 
"""

"""
문자열 바꾸기 
sub
"""
p = re.compile("(blue|white|red)")
print(p.sub("colour", "blue socks and red shoes"))

# 한번만 바꾸고 싶을떄
print(p.sub("colour", "blue socks and red shoes", count=1))

# 리턴을 튜플로
print(p.subn("colour", "blue socks and red shoes"))

"""
sub 메소드 사용 시 참조 구문
\g<그룹명> 사용
"""

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1> \g<1>", "park 010-1234-1234"))


"""
Greedy(탐욕스러운) vs Non-Greedy
"""
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group()) # <html><head><title>Title</title>

# non-greedy, 최소한의 반복 수행
print(re.match('<.*?>', s).group()) # <html>


# XML 문서 만들기
from xml.etree.ElementTree import Element, SubElement, dump
note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
dump(note) # <note><to>Tove</to></note>

note = Element("note")
to = Element("to")
to.text = "Tove"

note.append(to)
SubElement(note, "from").text = "Jani"
dump(note) # <note><to>Tove</to><from>Jani</from></note>

dummy = Element("dummy")
note.insert(1, dummy)
note.remove(to)
dump(note) # <note><dummy /><from>Jani</from></note>

note.attrib["date"] = "20190705"
dump(note) # <note date="20190705"><dummy /><from>Jani</from></note>

note = Element("note", date="20190705", age="123")
dump(note) # <note age="123" date="20190705" />

# indent
note = Element("note")
note.attrib["date"] = "20190705"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

def indent(elem, level=0):
	i = "\n" + level * " "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + " "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for elem in elem:
			indent(elem, level+1)
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
	else:
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = i

indent(note)
dump(note)

from xml.etree.ElementTree import ElementTree
ElementTree(note).write("note.xml")

from xml.etree.ElementTree import parse
tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))
print(note.get("foo", "default"))
print(note.keys())
print(note.items())

from_tag = note.find("from")
from_tags = note.findall("from")
from_text = note.findtext("from")

childs = note.getiterator()
childs = note.getchildren() # DeprecationWarning

print(note.getiterator("from"))

