FILEPATH = "files/todos.txt"

def read_todos(filepath=FILEPATH):
    """Read a text file and return the list of text items"""
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content


def write_todos(content, filepath=FILEPATH):
    """Write a list of text items to a file"""
    with open(filepath, 'w') as file:
        file.writelines(content)

if __name__ == "__main__":
    print("hello")
    print(read_todos())