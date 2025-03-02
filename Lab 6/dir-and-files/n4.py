def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"Number of lines in '{filename}': {len(lines)}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")

filename = "example.txt"
count_lines(filename)