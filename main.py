class Todo_list:
    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)
        print(f"{task} has been added to list.")

    def remove(self, task_remove):
        if self.task_list:
            self.task_list.remove(task_remove)
            print(f"{task_remove} has been removed.")
        else:
            print("Your list is empty.")

    def show_list(self):
        if self.task_list:
            for index, value in enumerate(self.task_list, start=1):
                print(f"#{index}. {value}")
        else:
            print("Your list is empty.")



todo_list = Todo_list()
todo_list.add("Eat")
todo_list.add("Sleep")
todo_list.add("Walk")
todo_list.show_list()
todo_list.remove("Eat")
todo_list.show_list()