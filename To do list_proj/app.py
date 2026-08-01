def task():
    tasks = []  # empty list
    print("-----------Welcome to the To-Do List App-----------")

    total_task = int(input("Enter the number of tasks you want to add: "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter the name of task {i}: ")
        tasks.append(task_name)

    print(f"Todays task are\n{tasks}")

    while True:

        opperation = int(input("ENTER\n1-ADD \n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))

        if opperation == 1:
            add = input("Enter the task u want to add: ")
            tasks.append(add)
            print(f"Task {add} has been successfuly added...")

        elif opperation == 2:
            updated_value = input("Enter the task name you want to update: ")

            if updated_value in tasks:
                up = input("Enter the new task: ")
                Index = tasks.index(updated_value)
                tasks[Index] = up
                print(f"Task {updated_value} has been updated to {up}.")
            else:
                print("Task not found.")

        elif opperation == 3:
            delete_val = input("Enter the task name you want to delete: ")

            if delete_val in tasks:
                Index = tasks.index(delete_val)
                # tasks.remove(delete)
                del tasks[Index]
                # delete = tasks.pop(Index)
                print(f"Task {delete_val} has been deleted.")
                print(f"Updated tasks: {tasks}")
        
            else:
                print("Task not found.")
      
        elif opperation == 4:
            print(f"Total_tasks = {tasks}")

        elif opperation == 5:
            print(" Here we go...Closing the Program...ENJOY NIGGA")
            break
    else:
        print("Invalid Input")


task()