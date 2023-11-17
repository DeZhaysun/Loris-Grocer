# File Name: employees.py
# Date: 2021-03-24
# This file just runs the employee functions when it is called from the main menu.
# The proper sql runs in the function file. Import error is there to ensure the user cannot product the wrong input and break the code
import sqlite3
from . import functions
from . import error

def printItems(items,position):
    '''Prints the items associated to an employee
    items - list of items
    position - in order for supervisors to not see other supervisor and owner info
    '''
    if items == 'Doesn\'t exist':
        print(items)
    else: 
        for item in items:
            if position == 'supervisor' and item[8] == 'cashier':
                print(f"\nrowID: {item[0]}\nFirst Name: {item[1]}\nLast Name: {item[2]}\nEmail: {item[3]}\nPhone Number: {item[4]}\nID: {item[5]}")
                print(f"Salary: ${item[6]}\nHire Date: {item[7]}\nPosition: {item[8]}\nReport To: {item[9]}\nPassword: {item[10]}\n")
            elif position == 'owner':
                print(f"\nrowID: {item[0]}\nFirst Name: {item[1]}\nLast Name: {item[2]}\nEmail: {item[3]}\nPhone Number: {item[4]}\nID: {item[5]}")
                print(f"Salary: ${item[6]}\nHire Date: {item[7]}\nPosition: {item[8]}\nReport To: {item[9]}\nPassword: {item[10]}\n")

viewMenu = '''How would you like to view the Employees?
        1. Last Name in Alphabetical Order
        2. Salary High to Low
        3. Salary Low to High
        4. ID Number
        5. Position Alphabetically
        6. By hire date
        7. Larger than or equal to inputted salary
        8. Smaller than or equal to inputted salary
        '''
def viewEmployee(position):
    '''
    The user is given multiple options to view all the employees based on a certain order. This order can be chosen by hitting 1-8
    Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input
    '''
    while True:
        
        print(viewMenu)
        viewEmployeeAns = input('Enter choice: ')
        if viewEmployeeAns == '1':
            items = functions.view('EMPLOYEE','lastName', True)
            printItems(items,position)
            break
        elif viewEmployeeAns =='2':
            items = functions.view('EMPLOYEE','salary', False)
            printItems(items,position)
            break
        elif viewEmployeeAns =='3':
            items = functions.view('EMPLOYEE','salary', True)
            printItems(items,position)
            break
        elif viewEmployeeAns =='4':
            items = functions.view('EMPLOYEE','idNumber', True)
            printItems(items,position)
            break
        elif viewEmployeeAns =='5':
            items = functions.view('EMPLOYEE','positionTitle', True)
            printItems(items,position)
            break
        elif viewEmployeeAns =='6':
            items = functions.view('EMPLOYEE','hireDate', True)
            printItems(items,position)
            break
        elif viewEmployeeAns =='7':
            items = functions.viewRange('EMPLOYEE','salary', True, 'Enter Salary: ')
            printItems(items,position)
            break
        elif viewEmployeeAns =='8':
            items = functions.viewRange('EMPLOYEE','salary', False, 'Enter Salary: ')
            printItems(items,position)
            break
        else:
            print("Enter a number from 1 to 8")
            functions.getchClear()
searchMenu = '''How would you look to search the employees?
        1. First Name
        2. Last Name
        3. Email
        4. Phone Number
        5. ID Number
        6. Salary
        7. Position
        8. Hire Date
        9. Report To
        10. rowID
        '''      
def searchEmployee(position):
    '''Searches for a specific employee or employees based on the information required from the user. This is chosen by  inputting a number 
    from 1 to 10. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input'''
    while True:
        
        print(searchMenu)
        
        searchEmployeeAns = input('Choose an option: ')

        if searchEmployeeAns == '1':
            items = functions.search('EMPLOYEE','firstName', 'string', 'Enter First Name: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '2':
            items = functions.search('EMPLOYEE','lastName', 'string', 'Enter Last Name: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '3':
            items = functions.search('EMPLOYEE','email', 'string', 'Enter Email: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '4':
            items = functions.search('EMPLOYEE','phoneNumber', 'int', 'Enter Phone Number: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '5':
            items = functions.search('EMPLOYEE','idNumber', 'int', 'Enter Employee ID: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '6':
            items = functions.search('EMPLOYEE','salary', 'float', 'Enter Employee Salary: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '7':
            items = functions.search('EMPLOYEE','positionTitle', 'string', 'Enter Title: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '8':
            items = functions.search('EMPLOYEE','hireDate', 'string', 'Enter the Hire Date: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '9':
            items = functions.search('EMPLOYEE','reportTo', 'string', 'Enter who the Employee Reports to: ' )
            printItems(items,position)
            break
        elif searchEmployeeAns == '10':
            items = functions.search('EMPLOYEE','rowID', 'int', 'Enter the rowID: ' )
            printItems(items,position)
            break
        else:
            print("Please enter a number from 1 to 10")
            functions.getchClear()
    
def addEmployee():
    '''Adds employees
    Gets input for all the columns in employee table, except the reportTo(can be automatically set) This does not have a loop or if statement
    because there are no options available when adding. The only if statement is two determine who they report to'''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()
    
    firstName = input('Enter first name: ')
    lastName = input('Enter last name: ')
    email = input('Enter email: ')
    phoneNumber = error.getPhone('Enter phone number: ')
    idNumber = error.getID('EMPLOYEE','idNumber','Enter ID number: ')
    salary = error.getFloat('Enter Salary: $')
    hireDate = error.getDate('Enter hire date (YYYY-MM-DD): ')
    positionTitle = (error.getPosition("Enter their Position Title(cashier, supervisor, owner): ")).lower()
    if positionTitle == 'cashier':
        reportTo = 'supervisor'
    elif positionTitle == 'supervisor':
        reportTo = 'owner'
    else:
        reportTo = ''
    password = input('Enter their Password: ')

    c.executemany("INSERT INTO EMPLOYEE VALUES (?,?,?,?,?,?,?,?,?,?)", [(firstName,lastName,email, phoneNumber, idNumber, salary, hireDate, positionTitle, reportTo, password)])

    conn.commit()
    conn.close()

removeMenu = '''How would you look to remove the employees?
        1. First Name
        2. Last Name
        3. Email
        4. Phone Number
        5. ID Number
        6. Salary
        7. Position
        8. Hire Date
        9. Report To
        10. rowID
        '''

def removeEmployee():
    '''
    removes a specific employee or employees based on the information required from the user. This is chosen by  inputting a number 
    from 1 to 10. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input
    '''
    while True:
        
        print(removeMenu)
        
        removeAns = input()

        if removeAns == '1':
            functions.remove('EMPLOYEE','firstName', 'string', 'Enter item First Name ' )
            break
        elif removeAns == '2':
            functions.remove('EMPLOYEE','lastName', 'string', 'Enter Last Name: ' )
            break
        elif removeAns == '3':
            functions.search('EMPLOYEE','email', 'string', 'Enter Email: ' )
            break
        elif removeAns == '4':
            functions.remove('EMPLOYEE','phoneNumber', 'int', 'Enter Phone Number: ' )
            break
        elif removeAns == '5':
            functions.remove('EMPLOYEE','idNumber', 'int', 'Enter Employee ID: ' )
            break

        elif removeAns == '6':
            functions.remove('EMPLOYEE','salary', 'float', 'Enter Salary: ' )
            break

        elif removeAns == '7':
            functions.remove('EMPLOYEE','hireDate', 'string', 'Enter Hire Date' )
            break

        elif removeAns == '8':
            functions.remove('EMPLOYEE','positionTitle', 'string', 'Enter Position: ' )
            break

        elif removeAns == '9':
            functions.remove('EMPLOYEE','reportTo', 'string', 'Enter who they Report To: ' )
            break
        elif removeAns == '10':
            functions.remove('EMPLOYEE','rowID', 'int', 'Enter rowID: ' )
            break
        else:
            print("Please enter a number from 1 to 10")
            functions.getchClear()

modifyItemMenu = '''What item would you like to modify?
        1. First Name
        2. Last Name
        3. Email
        4. Phone Number
        5. ID Number
        6. Salary
        7. Position
        8. Hire Date
        9. Report To
        '''

def modifyItem():
    '''Gets the column which will be modified based on the information required from the user. This is chosen by  inputting a number 
    from 1 to 10. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input. It will first ask how they want to search for the person, then what they want to modify from that employee'''
    while True:
        
        print(modifyItemMenu)

        modifyAns = input('Choose an option: ')

        if modifyAns == '1':
            modifyVar = 'firstName'
            modifyT = 'string'
            s1 = 'Enter new first name: '
            break
        elif modifyAns == '2':
            modifyVar = 'lastName'
            modifyT = 'string'
            s1 = 'Enter new last name: '
            break
        elif modifyAns == '3':
            modifyVar = 'email'
            modifyT = 'string'
            s1 = 'Enter new email: '
            break
        elif modifyAns == '4':
            modifyVar = 'phoneNumber'
            modifyT = 'int'
            s1 = 'Enter new phone number: '
            break
        elif modifyAns == '5':
            modifyVar = 'idNumber'
            modifyT = 'int'
            s1 = 'Enter new identification number: '
            break
        elif modifyAns == '6':
            modifyVar = 'salary'
            modifyT = 'float'
            s1 = 'Enter new salary: '
            break
        elif modifyAns == '7':
            modifyVar = 'hireDate'
            modifyT = 'string'
            s1 = 'Enter new hire date (YYYY-MM-DD): '
            break
        elif modifyAns == '8':
            modifyVar = 'positionTitle'
            modifyT = 'string'
            s1 = 'Enter new position title: '
            break
        elif modifyAns == '9':
            modifyVar = 'reportTo'
            modifyT = 'string'
            s1 = 'Enter new report to: '
            break
        else:
            print("Enter a number from 1 to 9")
            functions.getchClear()
    return [modifyVar, modifyT,s1]

modifyMenu = '''How would you look to search the employees?
        1. First Name
        2. Last Name
        3. Email
        4. Phone Number
        5. ID Number
        6. Salary
        7. Position
        8. Hire Date
        9. Report To
        10. rowID
        '''

def modifyEmployee():
    '''Gets the row that will be modified through user choice. 
    User chooses number 1 and 10
    Inside while loop to always get correct input'''
    while True:
        
        print(modifyMenu)
        
        modifyAns = input('Choose an option: ')


        if modifyAns == '1':
            searchBy = 'firstName'
            searchT = 'string'
            s = 'Enter first name: '
            break
        elif modifyAns == '2':
            searchBy = 'lastName'
            searchT = 'string'
            s = 'Enter last name: '
            break
        elif modifyAns == '3':
            searchBy = 'email'
            searchT = 'string'
            s = 'Enter email: '
            break
        elif modifyAns == '4':
            searchBy = 'phoneNumber'
            searchT = 'int'
            s = 'Enter phone number: '
            break
        elif modifyAns == '5':
            searchBy = 'idNumber'
            searchT = 'int'
            s = 'Enter identification number: '
            break
        elif modifyAns == '6':
            searchBy = 'salary'
            searchT = 'float'
            s = 'Enter salary: '
            break
        elif modifyAns == '7':
            searchBy = 'hireDate'
            searchT = 'string'
            s = 'Enter hire date (YYYY-MM-DD): '
            break
        elif modifyAns == '8':
            searchBy = 'positionTitle'
            searchT = 'string'
            s = 'Enter Position Title: '
            break
        elif modifyAns == '9':
            searchBy = 'reportTo'
            searchT = 'string'
            s = 'Enter report to: '
            break
        elif modifyAns == '10':
            searchBy = 'rowID'
            searchT = 'int'
            s = 'Enter rowID:  '
            break
        else:
            print("Enter a number from 1 to 10")
            functions.getchClear()
        
    modifyVar = modifyItem() #gets the column that will be modified
    functions.modify('EMPLOYEE', searchBy, modifyVar[0], searchT, modifyVar[1],s,modifyVar[2] )#modifies what the user wanted to modify
