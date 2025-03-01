import re

a = str(input())
b = re.compile(r'[a-z]+_[a-z]+')

c = b.finditer(a)
for i in c:
    print(i.group(0))