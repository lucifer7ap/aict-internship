class TodoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task[0]} - {'Completed' if task[1] else 'Pending'}")

    def add_task(self, task_name):
        self.tasks.append([task_name, False])
        print(f"Task '{task_name}' added!")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1][1] = True
            print(f"Task {task_number} completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print(f"Task {task_number} removed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nMenu:")
        print("1. Show To-Do List")
        print("2. Add a Task")
        print("3. Complete a Task")
        print("4. Remove a Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter task name: ")
            todo_list.add_task(task_name)
        elif choice == '3':
            todo_list.display_tasks()
            task_number = int(input("Enter task number to complete: "))
            todo_list.mark_completed(task_number)
        elif choice == '4':
            todo_list.display_tasks()
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '5':
            print("Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
