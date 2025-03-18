tasks = []

def addTask():
    task = input("please Enter a task ")
    tasks.append(task)
    print(f"Task '{task}' added to list")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task # {index}. {task}")


def deleteTask():
    listTasks()
    try:
        tasktodelete = int(input("Enter the number to delete"))
        if tasktodelete >=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"Task # {tasktodelete} has been removed")
        else:
            print(f"Task #{tasktodelete} was not found")
    except:
        print("Invalid input")
    

if __name__ == "__main__":
    ## create a loop to run the app
    print("Welcome to the to do list app :) ")
while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1.Add a new task")
    print("2. Delete a task")
    print("3. List")
    print("4. quit")

    choice = input("Enter yout choice: ")


    if(choice == "1"):
        addTask()
    elif(choice == "2"):
        deleteTask()
    elif(choice == "3"):
        listTasks()
    elif(choice == "4"):
        break
    else:
        print("Invalid input, Please try again")