def write_file(file_name, content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(content)

def append_file(file_name, content):
    with open(f"{file_name}.txt", "a") as file:
        file.write(content)

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
