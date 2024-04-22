

messege="""
1- add a new task
2- mark task as completed
3- view tasks 
4- Quit
"""

tasks=[]

# ------------------ start functions ---------------------------------
def add_task():
    task=input("Enter your task: ")
    task_info={"task": task, "completed":False}
    tasks.append(task_info)
    print("Task added to the list successfuly")

# ------------------

def mark_task_as_complete():
    taskName=input("Enter your task that you complete :")
    for task in tasks:
        if task["task"]==taskName:
            task["completed"]=True
            break   

# ------------------

def view_tasks():
    for task in tasks:
        for key, value in task.items():
            print(key, value)
        print("-----------------")


# ------------------ end functions ---------------------------------

while True:
    print(messege)
    choice=input("Enter your choice :")

    if choice =="1":
        add_task()

    elif choice=="2":
        mark_task_as_complete()

    elif choice=="3":
        view_tasks()

    elif choice=="4":
        break

    else:
        print("Invalid input , Enter a number between 1 and 4")
