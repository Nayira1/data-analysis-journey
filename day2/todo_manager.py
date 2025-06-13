print("MENU \n")
print("1 for adding a task\n")
print("2 for removing the task\n")
print("3 for viewing your todo list\n")
print("4 for ending\n")

tasks = []

while True:
    try :
          choice = int(input("Please enter your choice ").strip())
          if choice == 1:
            new_task = input("Please enter your task ").strip()
            tasks.append(new_task)
            print("Your task has been added")

          elif choice == 2:
            deleted_task = input("Please enter the task you want to delete ").strip()
            if deleted_task in tasks:
                tasks.remove(deleted_task)
                print("Your task has been removed.")
            else:
                print("Task not found.")
  
          elif choice == 3:
            print (tasks)

          elif choice == 4 :
            print ("Ending the program ")
            break

          else :
              print("Invalid choice, try again")

    except(ValueError, IndexError):
      print("Incorrect input, try again")
