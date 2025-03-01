import re
input_string = "hello_world_python"
output_string = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), input_string)
print(output_string)