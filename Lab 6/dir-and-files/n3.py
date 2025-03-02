import os

def check_path_and_split(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = "path"
check_path_and_split(path)