import re

a = str(input())
b = re.compile(r'[A-Z][a-z]+')

c = b.finditer(a)
for i in c:
    print(i.group(0))