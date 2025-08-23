# TO-DO List 
task = []
while True:
    print ('\n1.Add Task \n2.View Task \n3.Remove Task \n4.Exit')
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        task_name = input("Enter Task : ")
        task.append(task_name)
        print(task)
    elif choice ==2 :
         for i in task :
             print([i])
    elif choice == 3 :
        task_remove = input ("Enter task to remove : ")
        if task_remove in task :
            task.remove(task_remove)
            print("Task Removed")
        else :
            print("Task Not Found")
    elif choice == 4 :
        print("Exiting From To-Do List")
        break
    else :
        print("Enter Valid Choice")