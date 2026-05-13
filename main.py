from task import Task
from storage import Storage
from utils import print_menu

# Object Storage
storage = Storage()

# Load task từ JSON
tasks = storage.load_tasks()

# Generate id tự động
def generate_task_id():
    if not tasks:
        return 1
    # Lấy id cuối + 1
    return tasks[-1].id + 1

while True:
    print_menu()

    choice = input("Choose: ")

    # Add task
    if choice == "1":
        title = input("Enter task title: ")

        task = Task(
            generate_task_id(),
            title
        )

        tasks.append(task)

        storage.save_tasks(tasks)

        print("Task added!")

    # View task
    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)
    
    # Complete task
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print(task)
            
            try:
                task_id = int(input("Enter task id to complete: "))

                found = False
                # Tìm task
                for task in tasks:
                    # Nếu id trùng
                    if task.id == task_id:
                        task.mark_completed()

                        found = True

                        break
                
                if found:
                    storage. save_tasks(tasks)

                    print("Task Completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input.")
    
    # Delete task
    elif choice == "4":
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print(task)

            try: 
                task_id = int(input("Enter task id to delete: "))

                found = False

                for task in tasks:
                    if task.id == task_id:
                        tasks.remove(task)
                        found = True
                        break
                if found:
                    storage.save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Task not found.")
            
            except ValueError:
                print("Invalid input.")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid menu.")