import os

def generate_text_files():
    try:
        for letter in range(ord('A'), ord('Z') + 1):
            file_name = f"{chr(letter)}.txt"
            with open(file_name, 'w') as file:
                file.write(f"This is the content of {file_name}.")
        print("26 text files created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

generate_text_files()