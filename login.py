"""
Lab 1
Maya Griffith
CS 166 / Fall 2021
This is a prgram that allows you to log in and choose different menu options.
"""


#start not logged in and without a status
logged_in = False
status =  ""


#load_users function, takes a dictionary and loads a file into the dictionary for the usernames and passwords
#using the relative path to load the file because for some reason it would not work on my ide with the regular path
#key is the access level, and value consists of the username and password
def load_users(everyone):
    try:
        readfile = open('/Users/mayagriffith/Desktop/cybersecurity/users.txt', 'r')
    except IOError:
        print("could not open")
        exit()
    status = []
    for line in readfile:
        x = line.rstrip().rsplit(',')
        everyone[x[0]]= x[1]
    print (everyone)



#login function that takes the dictionary of data, and a username and password that the user inputs
#checks if the value matcaches with the username and password, and then if it does it retrives the key

def check_login(everyone, username, password):
    global logged_in
    global status
    for x, i in enumerate(everyone.values()): 
        if i == username + " " + password:
            logged_in=True
            keys = list(everyone.keys())
            status = keys[x]
            print(status)
            print ("You have logged in!")
        else:
            username=username


#master menu
def show_admin_menu():
    print("1) Accounting application")
    print("2) Enginering Documents")
    print("3) Time Entry")
    print("4) Read Manual")
    print("5) Place order")

def pick():
    choice = input("what is your choice?")
    return choice



#admin choice menu
def pick_admin_menu(choice):
    if choice == 1:
        return "You picked the accounting application"
    elif choice== 2:
        return "You picked the Enginering Documents"
    elif choice== 3:
        return "You picked the Time Entry"
    elif choice== 4:
        return "You picked the Company Manual"
    elif choice== 5:
        return "You picked place an order"
    else:
        menu = pick();
        if menu==6:
            show_admin_menu()
            pick_admin_menu(pick())
        else:
            exit()
        return "Oops, you didn't pick a menu option, press 6 to go back to main menu"
    



#employee choice menu
def pick_employee_menu(choice):
    if choice == 1:
        "You can't access this application. sorry. press 1 to go back to main menu"
        menu = pick();
        if menu==1:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()
    elif choice == 2:
        "You can't access this application. sorry press 1 to go back to main menu"
        menu = pick();
        if menu==1:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()
    elif choice == 3:
        "You picked the Time Entry"
    elif choice == 4:
        "You picked the Company Manual"

    elif choice == 5:
        "You picked place an order"

    else:
        "Oops, you didn't pick a menu option. press 6 to go back to main menu"
        menu = pick();
        if menu==6:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()

#customer choice menu
def pick_customer_menu(choice):
    if choice == 1:
        "You can't access this application. press 1 to go back to main menu"
        menu = pick();
        if menu==1:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()
    elif choice == 2:
        "You can't access this application. sorry. press 1 to go back to main menu"
        menu = pick()
        if menu==1:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()
    elif choice == 3:
        "You can't access this application. sorry. press 1 to go back to main menu"
        menu = pick()
        if menu==1:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()
    elif choice == 4:
        "You can't access this application. sorry. press 1 to go back to main menu"
        menu = pick()
        if menu==1:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()
    elif choice == 5:
        return "You picked place an order."
    else:
        "You didn't pick an option. press 6 to go back to main menu"
        menu = pick()
        if menu==6:
            show_admin_menu()
            pick_employee_menu(pick())
        else:
            exit()

def main():
    everyone = {}
    load_users(everyone)

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    global logged_in

    check_login(everyone, username, password)
    print(logged_in)
    if logged_in is True:
        #if the access level is admin
        print(status)
        if  status == "admin":
            show_admin_menu()
            choice = pick()
            pick_admin_menu(choice)
        elif status == "worker":
            show_admin_menu()
            choice = pick()
            pick_employee_menu(choice)
        else:
            show_admin_menu()
            choice = pick()
            pick_customer_menu(choice)
main()