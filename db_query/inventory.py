# File Name: inventory.py
# Date: 2021-03-24
# This file just runs the inventory functions when it is called from the main menu.
# The proper sql runs in the function file. Import error is there to ensure the user cannot product the wrong input and break the code
import sqlite3
from . import functions
from . import error

def printItems(items):
    if items == 'Doesn\'t exist':
        print(items)
    else: 
        for item in items:
            print(f"\nrowID: {item[0]}\nItem Name: {item[1]}\nItem Code: {item[2]}")
            print(f"Item Price: {item[3]}\nMore Info: {item[4]} \nItem stock: {item[5]}\n")

viewMenu = '''How would you like to view our Inventory:
        1. In Alphabetical Order
        2. Price High to Low
        3. Price Low to High
        4. Barcode Number
        5. Stock low to high
        6. Greater than or equal to inputted price
        7. Lesser than or equal to inputted price
        8. Greater than or equal to inputted stock
        9. Lesser than or equal to inputted stock
        '''

def viewInventory():
    '''
    Views a item in a certain order based on the response required from the user. This is chosen by  inputting a number 
    from 1 to 9. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input
    '''
    while True:
        
        print(viewMenu)
        viewInventoryAns = input('Enter choice: ')
        if viewInventoryAns == '1':
            items = functions.view('INVENTORY', 'itemName', True)
            printItems(items)
            break
        elif viewInventoryAns == '2':
            items = functions.view('INVENTORY', 'itemPrice', False)
            printItems(items)
            break
        elif viewInventoryAns == '3':
            items = functions.view('INVENTORY', 'itemPrice', True)
            printItems(items)
            break
        elif viewInventoryAns == '4':
            items = functions.view('INVENTORY', 'itemSerialNumber', True)
            printItems(items)
            break
        elif viewInventoryAns == '5':
            items = functions.view('INVENTORY', 'stock', True)
            printItems(items)
            break
        elif viewInventoryAns == '6':
            items = functions.viewRange('INVENTORY', 'itemPrice', True, 'Enter price: ')
            printItems(items)
            break
        elif viewInventoryAns == '7':
            items = functions.viewRange('INVENTORY', 'itemPrice', False, 'Enter price: ')
            printItems(items)
            break
        elif viewInventoryAns == '8':
            items = functions.viewRange('INVENTORY', 'stock', True, 'Enter stock: ')
            printItems(items)
            break
        elif viewInventoryAns == '9':
            items = functions.viewRange('INVENTORY', 'stock', False, 'Enter stock: ')
            printItems(items)
            break
        else:
            print("Please enter a number from 1 to 9")
            functions.getchClear()

searchMenu = '''How would you like to search the inventory
        1. Item Name
        2. Item Serial Code
        3. Item Price
        4. rowID
        5. Stock
        '''

def searchInventory():
    ''' Searches a specific item or items based on the information required from the user. This is chosen by  inputting a number 
    from 1 to 5. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input'''
    while True:
        
        print(searchMenu)
        searchAns = input('Choose an option: ')
        if searchAns == '1':
            items = functions.search('INVENTORY','itemName', 'string', 'Enter item name: ' )
            printItems(items)
            break
        elif searchAns == '2':
            items = functions.search('INVENTORY','itemSerialNumber', 'int', 'Enter item serial number: ' )
            printItems(items)
            break
        elif searchAns == '3':
            items = functions.search('INVENTORY','itemPrice', 'float', 'Enter item price: ' )
            printItems(items)
            break
        elif searchAns == '4':
            items = functions.search('INVENTORY','rowID', 'int', 'Enter item ID: ' )
            printItems(items)
            break
        elif searchAns == '5':
            items = functions.search('INVENTORY','stock', 'int', 'Enter the stock: ' )
            printItems(items)
            break
        else:
            print("Please enter a number from 1 to 5")
            functions.getchClear()
    

def addInventory():
    '''
    Gets input for all the columns in item table. This does not have a loop or if statement
    because there are no options available when adding.
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()

    itemName = (input("What is the Item Name? ")).lower()
    itemSerial = error.getInt("What is it's Serial Code? ")
    itemPrice = error.getFloat("What is the Price of this Item? $") 
    itemDescription = input("Any additional Info about this Item? " )
    stock = error.getInt("Enter the amount of stock for item: ")

    c.executemany("INSERT INTO INVENTORY VALUES (?,?,?,?,?)", [(itemName,itemSerial,itemPrice, itemDescription,stock)])

    print("SUCCESS")

    conn.commit()
    conn.close()

removeMenu = '''What would you like to remove:
        1. Item Name
        2. Item Serial Code
        3. Item Price
        4. Row ID
        5. Stock
        '''     

def removeInventory():
    '''
    Removes an item in a certain order based on the response required from the user. This is chosen by  inputting a number 
    from 1 to 5. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input
    '''
    while True:
          
        print(removeMenu)
        searchAns = input()
        if searchAns == '1':
            functions.remove('INVENTORY','itemName', 'string', 'Enter item name: ' )
            break
        elif searchAns == '2':
            functions.remove('INVENTORY','itemSerialNumber', 'int', 'Enter item serial number: ' )
            break
        elif searchAns == '3':
            functions.search('INVENTORY','itemPrice', 'float', 'Enter item price: ' )
            break
        elif searchAns == '4':
            functions.remove('INVENTORY','rowID', 'int', 'Enter item ID: ' )
            break
        elif searchAns == '5':
            functions.remove('INVENTORY','stock', 'int', 'Enter item stock: ' )
            break
        else:
            print("Please enter a number from 1 to 5")
            functions.getchClear()

modifyItemMenu = '''What item would you like to modify?
        1. Item Name
        2. Item Serial Code
        3. Item Price
        4. Stock
        '''    

def modifyItem():
    '''  Gets the column which will be modified based on the information required from the user. This is chosen by  inputting a number 
    from 1 to 4. Like other functions it uses a series of if statements to determine how to place it. It is placed in a while loop so it will 
    always get a valid input'''
    while True:
        
        print(modifyItemMenu)
        modifyAns = input()
        if modifyAns == '1':
            modifyVar = 'itemName'
            modifyT = 'string'
            s1 = 'Enter new name: '
            break
        elif modifyAns == '2':
            modifyVar = 'itemSerialNumber'
            modifyT = 'int'
            s1 = 'Enter new serial number:  '
            break
        elif modifyAns == '3':
            modifyVar = 'itemPrice'
            modifyT = 'float'
            s1 = 'Enter new price; '
            break
        elif modifyAns == '4':
            modifyVar = 'stock'
            modifyT = 'int'
            s1 = 'Enter new stock: '
            break
        else:
            print("Please enter a number from 1 to 4")
            functions.getchClear()
    return [modifyVar, modifyT,s1]
    
modifyMenu = '''How would you like to search for the item?
        1. Item Name
        2. Item Serial Code
        3. Item Price
        4. rowID
        5. Stock
        '''

def modifyInventory():
    '''Gets the row that will be modified through user choice. 
    User chooses number 1 and 5
    Inside while loop to always get correct input
    '''
    while True:
        
        print(modifyMenu)
        modifyAns = input()
        if modifyAns == '1':
            searchBy = 'itemName'
            searchT = 'string'
            s = 'Enter item name: '
            break
        elif modifyAns == '2':
            searchBy = 'itemSerialNumber'
            searchT = 'int'
            s = 'Enter item serial number: '
            break
        elif modifyAns == '3':
            searchBy = 'itemPrice'
            searchT = 'float'
            s = 'Enter item price: '
            break
        elif modifyAns == '4':
            searchBy = 'rowID'
            searchT = 'int'
            s = 'Enter rowID: '
            break
        elif modifyAns == '5':
            searchBy = 'stock'
            searchT = 'int'
            s = 'Enter item stock: '
            break
        else:
            print("Please enter a number from 1 to 5")
            functions.getchClear()
        
    modifyVar = modifyItem() #gets the specific column that will be modified

    functions.modify('INVENTORY', searchBy, modifyVar[0], searchT, modifyVar[1],s,modifyVar[2])#modifies what the user wanted to modify