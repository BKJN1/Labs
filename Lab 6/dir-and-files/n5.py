def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"List written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "output.txt"
data_list = ["Apple", "Banana", "Cherry", "Date"]
write_list_to_file(file_path, data_list)