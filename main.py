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

# Search task theo keyword
def search_tasks(tasks):
    if not tasks:

        print("No task found.")

        return
    
    keyword = input("Enter keyword: ").lower()
    
    # flag kiểm tra có kết quả không
    found = False

    print("\n=== SEARCH RESULT ===")

    # loop từng task
    for task in tasks:
        #search không phân biệt hoa thường
        if keyword in task.title.lower():
            print(task)
            found = True
    
    if not found:
        print("No matching tasks")

# Filter task theo trạng thái
def filter_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n1. Completed")
    print("2. Uncompleted")
    
    # User chọn filter
    choice = input("Choose filter: ")

    # Completed
    if choice == "1":
        print("\n=== COMPLETED TASKS ===")

        found = False

        for task in tasks:
            #Chỉ lấy completed=True
            if task.completed:
                print(task)
                found = True
        
        if not found:
            print("No completed tasks.")
    
    elif choice == "2":
        print("\n=== UNCOMPLETED TASKS ===")
        found = False

        for task in tasks:
            # Chỉ lấy completed=False
            if not task.completed:
                print(task)
                found = True
        
        if not found:
            print("No uncompleted tasks.")
    
    else:
        print("Invalid filter.")

while True:
    print_menu()

    choice = input("Choose: ")

    # Validate input
    if choice not in["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid menu.")
        # quay lại đầu loop
        # return to the begining of the loop
        continue

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

    # Search
    elif choice == "5":
        search_tasks(tasks)
        break

    # Filter
    elif choice == "6":
        filter_tasks(tasks)
        break

    # Exit
    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid menu.")

