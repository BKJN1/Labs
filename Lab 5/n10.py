import re
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', camel_str).lower()

input_string = "HelloWorldPython"
print(camel_to_snake(input_string))