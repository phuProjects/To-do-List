print("Welcome to your To-do list!")

def addTask():
    task = input("Add your task here: ")
    todo_list.append(task)

def removeTask():
    listTask()
    remove = int(input("The task you wanna remove (#): "))
    todo_list.pop(remove-1)
    print(f"Task #{remove} has been removed.")
    
def listTask():
    print("\nHere are your tasks: ")
    for i, val in enumerate(todo_list, start=1):
        print(f"#{i}. {val}")

todo_list = []
run = True

while run:
    print("\nSelect the follow option: ")
    print("------------------")
    print("1. add task")
    print("2. remove task")
    print("3. list the tasks")
    print("4. Quit")
    option = int(input("Choice: "))
    
    if option == 1:
        addTask()
    elif option == 2:
        removeTask()
    elif option == 3:
        listTask()
    elif option == 4:
        run = False

print("\nGoodbye!")