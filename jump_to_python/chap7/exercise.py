# 정규 표현식
## Q1

import re
p = re.compile("a[.]{3,}b")
print(p.match("acccb"))
print(p.match("a...b"))
print(p.match("aaab"))
print(p.match("a.cccb"))

p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start(), m.end())

phonelist = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8787-7768
"""

p = re.compile(r"(?P<start>\w+\s\d+[-]\d+[-])\d+")
m = p.search(phonelist, re.MULTILINE)
print(p.sub("\g<1>****", phonelist))


p = re.compile(".*[@].*[.](?=com$|net$).*$")

m = p.match("park@naver.com")
print(m.group())

m = p.match("kim@daum.net")
print(m.group())

m = p.match("lee@myhome.co.kr")
print(m)

from xml.etree.ElementTree import Element, SubElement, dump, ElementTree
blog = Element("blog")
blog.attrib["date"]="20151231"

subject = Element("subject")
subject.text = "WhyPython"
blog.append(subject)

# author = Element("author")
# author.text = "Eric"
# blog.append(author)
SubElement(blog, "author").text = "Eric"
SubElement(blog, "content").text = "Life is to Short, You need Python!"

ElementTree(blog).write("blog.xml")