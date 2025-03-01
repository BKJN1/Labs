import re

a = str(input())
b = re.sub(r'[ ,.]', ':', a)
print (b)