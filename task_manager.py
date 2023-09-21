#=====importing libraries===========
# Create blank lists to store inputs for usernames and passwords
username = []
password = []

with open("user.txt", "r") as file_user:
    for lines in file_user:
        user = lines.strip()
        user = user.split(', ')
        username.append(user[0])
        password.append(user[-1])
file_user.close()

#====Login Section====

# Create a log in section for the user 
# The program must stop the user if they have entered an incorrect username or password
# Only when the correct username and password combination is entered can the program progress to the main menu
# Request username and only request password if the username is in registered the user.txt file

username_input = input("Please enter your username: ")
while username_input not in username:
    print("The username you have entered does not exist")
    username_input = input("Please enter your username: ")
else:
    pass
    password_input = input("Please enter your password: ")
    while password_input not in password:
        print("The password you have entered is incorrrect")
        password_input = input("Please enter your password: ")
    else:
# The program must only allow the correct password to be used with the entered username
        while username.index(username_input) != password.index(password_input):
            print("The password is incorrect")
            password_input = input("Please enter your password: ")
        else:
            pass


while True:
    if username_input == "admin":
#presenting the menu to the user and 
# making sure that the user input is coneverted to lower case.
# The admin user only will have access to the vs option to view number of users and tasks
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
vs - View Stats
: ''').lower()
    else:
                menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
                
# Only the admin user is allowed to register a new user 
    if menu == 'r':
        if username_input == "admin":
            pass
            new_user = input("Please enter a new username: ")
            if new_user in username:
                print("Sorry, this username already exists")
            else:
                new_password = input("Please enter a new password: ")
                if new_password in password:
                    print("Sorry, this password already exists")
                else:
                    confirm_password = input("Please enter your password again: ")
                    if new_password == confirm_password:
                        file_user = open("user.txt", "a")
                        file_user.write(f"\n{new_user}, {new_password}")
                        file_user.close()
                    else:
                        print("Sorry, your passwords do not match")
        else:
            print("Sorry, only user 'admin' can register new users")
    elif menu == 'a':
        pass
#Request from the user all the data that needs to go into the new task
        username_add = input("Please enter your username of the person: ")
        task_title = input("Please enter the task title: ")
        task_desc = input("Please enter the task description: ")
        date = input("Please enter today's date: ")
        due_date = input("Please enter the due date: ")

# Open the task file and write a new line from the inputs above
        file_task = open("tasks.txt", "a")
        file_task.write(f"\n{username_add}, {task_title}, {task_desc}, {date}, {due_date}, No")
        file_task.close()

# Read all the tasks in the task.txt file and present in an easy to read manner 
    elif menu == 'va':
        pass
        file_task = open("tasks.txt", "r")
        file_task.readlines
        for lines_task in file_task:
            task = lines_task.strip()
            task = lines_task.split(', ')
            print(f"\nTask: {task[1]}\nAssigned to: {task[0]}\nDate assigned: {task[3]}\nDue date: {task[4]}\nTask completed: {task[5]}")
        file_task.close()

# Only the tasks for the user that is logged in must be displayed in an easy to read manner
    elif menu == 'vm':
        pass
        file_task = open("tasks.txt", "r")
        file_task.readlines
        for lines_task in file_task:
            task = lines_task.strip()
            task = lines_task.split(', ') 
            if username_input in task:
                if username_input == task[0]:
                    print(f"\nTask: {task[1]}\nDate assigned: {task[3]}\nDue date: {task[4]}\nTask completed: {task[5]}")
                else:
                    print("The username you have entered is incorrect")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    elif menu == 'vs':
# Calculate the amount of users using a for loop 
        total_users = 0
        file_user = open("user.txt", "r")
        file_user.readlines
        for num_users in file_user:
            total_users += 1
        print(f"Total number of users: {total_users}")
        file_user.close()
# Calculate the amount of tasks using a for loop
        total_tasks = 0
        file_task = open("tasks.txt", "r")
        file_user.readlines
        for num_tasks in file_task:
            total_tasks += 1
        print(f"Total number of tasks: {total_tasks}")
        file_task.close()

    else:
        print("You have made a wrong choice, Please Try again")