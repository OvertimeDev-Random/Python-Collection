def ToDoList():
    class TodoList:
        def __init__(self):
            self.tasks = []

        def add_task(self, task):
            self.tasks.append(task)
            print(f'Task "{task}" added.')

        def view_tasks(self):
            if not self.tasks:
                print("No tasks available.")
            else:
                print("Tasks:")
                for i, task in enumerate(self.tasks, 1):
                    print(f"{i}. {task}")

        def remove_task(self, task_index):
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                print(f'Task "{removed_task}" removed.')
            else:
                print("Invalid task index.")

    def main():
        todo_list = TodoList()

        while True:
            print("\nOptions:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                task = input("Enter the task: ")
                todo_list.add_task(task)
            elif choice == "2":
                todo_list.view_tasks()
            elif choice == "3":
                task_index = int(input("Enter the task index to remove: "))
                todo_list.remove_task(task_index)
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    if __name__ == "__main__":
        main()