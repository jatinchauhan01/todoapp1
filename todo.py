# To-Do App


tasks = []

while True:

    
    print("\n--- TO DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            delete_task = int(input("Enter task number to delete: "))

            if delete_task > 0 and delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    
    elif choice == "4":
        print("Exiting To-Do App. Goodbye!")
        break

    
    else:
        print("Invalid choice. Please select 1-4.")
