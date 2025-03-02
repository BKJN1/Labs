import os

def list_directories_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nAll Directories and Files:")
    for entry in os.listdir(path):
        print(entry)

path = "Lab 5"
list_directories_files(path)