def open_todos(filepath):
    with open(filepath, "r") as f:
        todos = f.readlines()
        return todos
    

def write_todos(todos):
    with open("todos.txt", "w") as f:
        for todo in todos:
            f.writelines(todo)
