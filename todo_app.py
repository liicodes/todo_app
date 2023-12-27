def main():
    print("""What would you like to do? \n
    1. Add a task. \n
    2. Check all tasks. \n
    3. Remove a task. \n
    4. Exit. \n
    Please input a Number.""")

    while True:
        chgopt = input()

        if chgopt == "1":
            add(all_tasks)

        elif chgopt == "2":
            view(all_tasks)

        elif chgopt == "3":
            rmtask(all_tasks)

        elif chgopt == "4":
            print("Please do come back!")
            break

        else:
            print("Please enter a valid number.")


def add(all_tasks):
    a = len(all_tasks)
    task = input("Specify the task below: \n")
    all_tasks.append(f"{a + 1}. {task}")
    print("New task has been added!")


def view(all_tasks):
    print("Tasks: \n")
    for i in all_tasks:
        print(f"{i} \n")


def rmtask(all_tasks):
    view(all_tasks)
    rmopt = int(input("Please enter the number of the task you'd like to remove: \n"))
    if 1 <= rmopt <= len(all_tasks):
        all_tasks.pop(rmopt - 1)
        print("Task removed successfully!")
    else:
        print("Invalid task number. Please enter a valid number.")


if __name__ == '__main__':
    all_tasks = []
    print("Hello welcome to your personal To Do App \n")
    main()
