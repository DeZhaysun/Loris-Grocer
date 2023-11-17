# File Name: main.py
# Date: 2021-03-24
# File Description:
# main.py diplays all the menus and sub menus and starts the chain reaction of calling functions
# There is absolutely no sql in this file. We import employee, inventory, and functions
# to call their respective files. We import time just to be able to create a delay for the Description down. Finally the functions file is primarly used to call clear and getch which 
# clear the screen for the user and waits for user to hit enter
#All the submenues have the parameter position, in order for the program to know who is accessing the database, and restricts certain functions based on position

import employee
import inventory
import sales
import functions
import encryption
import time

def lorisSign(first):
    """
    This function creates the epic Loris drop down menu
    """
    print("\033[1;32;40m ===================================================================")
    if first: time.sleep(0.2)
    print(' __             __________    ___________     ___   _   __________  ')
    if first: time.sleep(0.2)
    print("|  |           |          |  |    ___    |   |   | |_| |          | ")
    if first: time.sleep(0.2)
    print('|  |           |   ____   |  |   |   |   |   |   |     |  ________| ')
    if first: time.sleep(0.2)
    print('|  |           |  |    |  |  |   |___|   |   |   |     | |________  ')
    if first: time.sleep(0.2)
    print('|  |           |  |    |  |  |         __/   |   |     |_______   | ')
    if first: time.sleep(0.2)
    print('|  |           |  |    |  |  |    _    \     |   |             |  | ')
    if first: time.sleep(0.2)
    print('|  |_________  |  |____|  |  |   | \    \    |   |      _______|  | ')
    if first: time.sleep(0.2)
    print('|            | |          |  |   |  \    \   |   |     |          | ')
    if first: time.sleep(0.2)
    print('|____________| |__________|  |___|   \____\  |___|     |__________| ')
    if first: time.sleep(0.2)
    print("===================================================================")
    
main_Menu = '''-------------------------------------------
| Welcome to the Main Menu                |
| Please choose one of the options below: |
|   1. Inventory                          |
|   2. Employee                           |
|   3. Sales                              |
|   4. Sign Out                           |
-------------------------------------------'''

def mainMenu(first, position):
    """
    Displays the main menu and leads the user to the sub menu by using the numbers
    1 to 4
    """
    while True:
        lorisSign(first)
        
        print(main_Menu)
        
        mainAns = input("What would you like to Choose: ")
        if mainAns == '1':
            functions.clear()
            inventoryMenu(position)
            return True
        elif mainAns == '2':
            if position == "cashier":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                employeeMenu(position)
                return True
        elif mainAns == '3':
            functions.clear()
            salesMenu(position)
            return True
        
        elif mainAns == '4':
            print("Press any button to exit")
            functions.getchClear()
            return False
        else:
            print("Wrong Input")
            print('Type anything to continue')
            functions.getchClear()

menuInventory = '''Please choose one of the options below:
        1. View Inventory
        2. Search Inventory
        3. Add to Inventory 
        4. Remove from Inventory 
        5. Modify from Inventory 
        6. Exit to Main Menu
        '''

def inventoryMenu(position):
    """
    This is similiar to the main menu but it used to navigate the inventory. It also
    requires numbers in order for the user to make a decision It will loop until it gets 
    a number from 1 to 4
    """
    while True:
        
        print(menuInventory)

        answerInventory = input('Enter Choice: ')

        if answerInventory == '1':
            
            functions.clear()
            inventory.viewInventory()
            print('')
            print("Press any button to exit")
            functions.getchClear()
            break

        elif answerInventory == '2':
            functions.clear()
            inventory.searchInventory()
            print('')
            print("Press any button to exit")
            functions.getchClear()
            break
        elif answerInventory == '3':
            
            if position == "cashier" or position == "supervisor":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                inventory.addInventory()
                print('')
                print("Press any button to exit")
                functions.getchClear()
                break
        elif answerInventory == '4':
            if position == "cashier" or position == "supervisor":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                inventory.removeInventory()
                print('')
                print("Press any button to exit")
                functions.getchClear()
                break
        elif answerInventory == '5':
            if position == "cashier":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                inventory.modifyInventory()
                print('')
                print("Press any button to exit")
                functions.getchClear()
                break
        elif answerInventory == '6':
            print("Press any button to exit")
            functions.getchClear()
            break
        else:
            print("Please input a number from one to four")
            print('Type anything to continue')
            functions.getchClear()

employee_menu = '''Please choose one of the options below:
        1. View Employees
        2. Search Employees
        3. Add Employee
        4. Remove Employee
        5. Modify Employee
        6. Exit Menu
        '''

def employeeMenu(position):
    """
    This function is the same as inventory in the sense it displays
    the options for the sub menus and takes in a number in order 
    to call the appropriate function to carry out the task.
    If they do not enter a number from one to six the program will
    ask them again
    """
    while True:
        
        print(employee_menu)

        choice = input('Please select an option: ')
        if choice  == '1':
            functions.clear()
            employee.viewEmployee(position)
            print("Press any button to exit")
            functions.getchClear()
            break
        elif choice == '2':
            functions.clear()
            employee.searchEmployee(position)
            print("Press any button to exit")
            functions.getchClear()
            break
        elif choice == '3':
            if position == "supervisor":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                employee.addEmployee()
                print("Press any button to exit")
                functions.getchClear()
                break
        elif choice == '4':
            if position == "supervisor":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                employee.removeEmployee()
                print("Press any button to exit")
                functions.getchClear()
                break
        elif choice == '5':
            if position == "supervisor":
                print("You do not have access to this section")
                functions.getchClear()
            else:
                functions.clear()
                employee.modifyEmployee()
                print("Press any button to exit")
                functions.getchClear()
                break
        elif choice == '6':
            print("Press any button to exit")
            functions.getchClear()
            break
            
        else:
            print("Invalid input, please try again.")
            functions.getchClear()
            print('Type anything to continue')

sales_menu = '''Please choose one of the options below:
        1. View Sales
        2. Search Sales
        3. Add Sales
        4. Exit Menu
        '''

def salesMenu(position):
    """
    Once again it is the same concept as employee and inventory. You 
    are given 4 choices and choose between the 4 choices by providing a number from 1 to 4. It will keep on nagging you to enter a number 
    from one to four if you do not.
    """
    while True:
        
        print(sales_menu)
        
        choice = input('Please select an option: ')
        if choice  == '1':
            functions.clear()
            sales.viewSales()
            print("Press any button to exit")
            functions.getchClear()
            break
        elif choice == '2':
            functions.clear()
            sales.searchSales()
            print("Press any button to exit")
            functions.getchClear()
            break
        elif choice == '3':
            functions.clear()
            sales.addSales()
            print("Press any button to exit")
            functions.getchClear()
            break
        elif choice == '4':
            print("Press any button to exit")
            functions.getchClear()
            break

        else:
            print("Invalid input, please try again.")
            print('Type anything to continue')
            functions.getchClear()
            

mainMenuCondition = True
subMenuCondition = True
first = True

#This is what gets the whole program started. It first calls on 
# encryption then it calls on the main menu until the user is on the main menu and decides to hit sign out. First is there in order to speed up the Loris 
#menu drop down for the first time. After the first time it  gets long and grueling

while True:
    position = encryption.signIn()
    while mainMenuCondition:
        mainMenuCondition = mainMenu(first, position)
        first = False
    mainMenuCondition = True
    