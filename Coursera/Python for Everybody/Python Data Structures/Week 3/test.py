import re

text = "this is just a test 151513"


x = re.search(r"this is just a test\s(\d*)", text)
print(x.group(1))