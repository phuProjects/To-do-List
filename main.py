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

    def clear_list(self):
        if self.task_list:
            self.task_list.clear()
        else:
            print("Your list is already empty.")

    def load_task(self,file_name):
        with open(file_name, 'r') as file:
            self.task_list = [line.strip() for line in file]
            print("Tasks has been loaded.")

    def save_task(self,file_name):
        with open(file_name, 'w') as file:
            for task in self.task_list:
                file.write(f"{task}\n")
        print("Your tasks has been saved.")



daily_todo_list = Todo_list()
daily_todo_list.add("work")
daily_todo_list.add("read")
daily_todo_list.add("run")

daily_todo_list.save_task("dailyTasks.txt")
daily_todo_list.load_task("dailyTasks.txt")

weekend_todo_list = Todo_list()
weekend_todo_list.add("Sleep")
weekend_todo_list.add("Game")
weekend_todo_list.add("Eat")

weekend_todo_list.save_task("weekendTasks.txt")
weekend_todo_list.load_task("weekendTasks.txt")

daily_todo_list.show_list()
weekend_todo_list.show_list()


