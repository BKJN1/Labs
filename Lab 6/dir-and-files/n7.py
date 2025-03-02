def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            with open(destination_path, 'w') as destination_file:
                destination_file.write(source_file.read())
        print(f"Contents of '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"The file '{source_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_path = "source.txt"
destination_path = "destination.txt"
copy_file(source_path, destination_path)