import re

a = str(input())
b = re.compile(r'a.*b$')

c = b.finditer(a)
for i in c:
    print(i.group(0))