import re
input_string = "HelloWorldPython"
result = re.sub(r'([A-Z])', r' \1', input_string).strip()
print(result)