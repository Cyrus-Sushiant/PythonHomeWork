import ToDoList


if __name__ == "__main__":
    to_do_list = ToDoList.ToDoList()
    
    print("1. Show all tasks")
    print("2. Add new task")
    print("3. Remove task")
    print("----------------")
    menu = input("Enter number of menu:")
    
    if (menu == "1"):
        print("Show all tasks: ")
        for task in to_do_list.show_all_tasks():
            print(task.name, task.description, task.priority)
    elif (menu == "2"):
        name = input("Enter name:")
        description = input("Enter description:")
        priority = input("Enter priority:")
        to_do_list.add_task(name, description, priority)
        print("Show all tasks: ")
        for task in to_do_list.show_all_tasks():
            print(task.name, task.description, task.priority)
    elif (menu == "3"):
        name = input("Enter name:")
        to_do_list.remove_task(name)
        print("Show all tasks: ")
        for task in to_do_list.show_all_tasks():
            print(task.name, task.description, task.priority)
