def get_todo():
    with open("todo.txt", "r") as file:
        todo_list = file.readlines()
    return todo_list

def add_todo(item):
    with open("todo.txt", "a") as file:
        file.write(f"{item}\n")
        