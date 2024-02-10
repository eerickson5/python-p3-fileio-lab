def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w") as my_file:
        my_file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as my_file:
        my_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", mode="r") as my_file:
        return(my_file.read())
