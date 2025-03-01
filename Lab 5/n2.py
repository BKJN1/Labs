import re

a = str(input())
b = re.compile(r'ab{2,3}')

c = b.finditer(a)
for i in c:
    print(i.group(0))