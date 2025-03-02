import os

def check_path_access(path):
    print(f"Existence: {os.path.exists(path)}")
    print(f"Readability: {os.access(path, os.R_OK)}")
    print(f"Writability: {os.access(path, os.W_OK)}")
    print(f"Executability: {os.access(path, os.X_OK)}")

path = "Lab 5"
check_path_access(path)