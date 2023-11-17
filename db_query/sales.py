# File Name: sales.py
# Date: 2021-03-24
# This file just runs the sales functions when it is called from the main menu.
# The proper sql runs in the function file. Import error is there to ensure the user cannot product the wrong input and break the code

import sqlite3
from . import functions
from . import error

def printItems(items):
    """
    Rather then typing out this same code over and over again there is a print items function
    which prints out the items attributes. This makes the program require less lines and makes it more efficient
    """
    if items == 'Doesn\'t exist':
        print(items)
    else: 
        for item in items:
            print(f"\nrowID: {item[0]}\nDate and Time: {item[1]}\nProduct(s) sold: {item[2]}\nEmployee: {item[3]}\nPayment Info: {item[4]}")
            print(f"No. of product(s) sold: {item[5]}\nAmount Made: {item[6]}\nOther info: {item[7]}\n")

viewMenu = '''How would you like to view the sales?
        1. Amount Made Low to High
        2. Amount Made High to Low
        3. Date and Time (Most Recent Sale)
        4. Date and Time (Earliest Sale)
        '''

def viewSales():
    """
    This function asks the user whether they want to view all the items in the menu in the 4 arrangements provided
    They can choose from 1 to 4. If they do not put the correct input it will loop till they do
    """
    
    while True:        
        print(viewMenu)
        viewInventoryAns = input('Enter choice: ')

        if viewInventoryAns == '1':
            items = functions.view('SALES', 'amountMade', True)
            printItems(items)
            break
        elif viewInventoryAns == '2':
            items = functions.view('SALES', 'amountMade', False)
            printItems(items)
            break
        elif viewInventoryAns == '3':
            items = functions.view('SALES', 'dateTime', False)
            printItems(items)
            break
        elif viewInventoryAns == '4':
            items = functions.view('SALES', 'dateTime', True)
            printItems(items)
            break
        else:
            print("Please enter a number from 1 to 4")
            functions.getchClear()

searchMenu = '''How would you like to search sales?
        1. Search Through Date (YYYY-MM-DD)
        2. Search Through Date and Time (YYYY-MM-DD HH:MM)
        3. Search through product
        4. Search Through cashier
        5. Search Through payment Info
        6. Search Through Amount Made
    '''

def searchSales():
    """
    This function asks the user whether they want to search the items in the menu in the 6 descriptions provided
    They can choose from 1 to 6. If they do not put the correct input it will loop till they do. 
    """
    
    while True:
        print(searchMenu)
        viewSalesAns = input('Enter choice: ')

        if viewSalesAns == '1':
            items = searchDate()
            printItems(items)
            break
        elif viewSalesAns == '2':
            items = functions.search('SALES','dateTime','string','Enter Date and Time(YYYY-MM-DD HH:MM): ')
            printItems(items)
            break
        elif viewSalesAns == '3':
            items = searchProduct()
            printItems(items)
            break
        elif viewSalesAns == '4':
            items = functions.search('SALES','employee','int','Enter employee ID')
            printItems(items)
            break

        elif viewSalesAns == '5':
            items = functions.search('SALES','payment','string','Enter payment information: ')
            printItems(items)
            break

        elif viewSalesAns == '6':
            items = functions.search('SALES','amountMade','float','Enter amount made: ')
            printItems(items)
            break

def addSales():
    """
    This function asks the user what they want to add to sales. This goes from date and time, the product sold, the amount made, 
    the person who made the sale, the payment, and the amount sold. There are not any options provided because you can only add one way.
    """
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()

    dateTime = error.getDateTime("What was the date and time for sale?  (YYYY-MM-DD HH:MM): ")
    
    productID = True #boolean to get the product id(s)

    while productID:
        productsSold = input("Enter product ids seperated by spaces: ")
        products = productsSold.split() #splits the ids into a list
        length = len(products)
        
        try:
            products = [int(i) for i in products] #turns the ids into integers
        except:
            print('Enter integers seperated by spaces')
        else:
            exists = True
            amount = []
            for i in products:
                c.execute("SELECT stock FROM INVENTORY WHERE itemSerialNumber = (?)", (i,))
                if c.fetchone(): #see if id exists
                    c.execute("SELECT stock FROM INVENTORY WHERE itemSerialNumber = (?)", (i,))
                    item = c.fetchall() 
                    amount.append(item)#gets and adds the stock for item
                else: #otherwise, id doesnt exis
                    print(str(i) + ' is not an item in the inventory.')
                    exists = False
                    break
            if exists:
                break

    cashier = getCashier()

    payment = input('Enter payment method: ')

    while True:
        nOfProductsSold = input("Enter the amount sold(integers) seperated by spaces: " )
        nOfProducts = nOfProductsSold.split()

        if len(nOfProducts) != length:
            print('Not enough or too many numbers') #when there isn't enough or too many amounts
        else:
            try:
                nOfProducts = [int(i) for i in nOfProducts] #turns it into numbers
            except:
                print('Enter integers seperated by spaces')
            else:
                larger = True
                amountMade = 0.0
                for i in range(length):
                    if amount[i][0][0] < nOfProducts[i]: #when u try to buy more than available
                        larger = False
                        print('No. of Items sold exceeds the no. of items available')
                        break
                    else:
                        newAmount = amount[i][0][0]
                        newAmount -= nOfProducts[i]

                        c.execute(f"UPDATE INVENTORY SET stock = {newAmount} WHERE itemSerialNumber = (?)", (int(products[i]),)) #updates the stock

                        c.execute("SELECT itemPrice FROM INVENTORY WHERE itemSerialNumber = (?)", (int(products[i]),))
                        price = c.fetchall() #gets the price
                        
                        amountMade += price[0][0] * nOfProducts[i] #add to amount made

                if larger:
                    break

    other = input("Add any additional info about the Sale: ")

    c.executemany("INSERT INTO SALES VALUES (?,?,?,?,?,?,?)", [(dateTime,productsSold,payment,cashier, nOfProductsSold,amountMade ,other)])
    
    conn.commit()
    conn.close()

def searchDate():
    '''Searches for sales on a user inputted date'''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()

    dateTime = error.getDate('Enter Date: ')

    c.execute(f"SELECT rowID, * FROM SALES WHERE dateTime LIKE {dateTime}%" )

    items = c.fetchall()

    conn.commit()
    conn.close()

    return items

def searchProduct():
    '''Searches for all the sales in which a user inputted product was sold'''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()

    code = error.getInt('Enter item code: ')

    c.execute(f"SELECT rowID, * FROM SALES WHERE product LIKE '%{code}%'" )

    items = c.fetchall()

    conn.commit()
    conn.close()

    return items

def getCashier():
    '''Gets the cashier/employee that conducted the sale
    checks to make sure the employee exists in the database'''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()
    while True:
        cashier = error.getInt("Enter Employee ID of the person who made the sale: ")
        c.execute("SELECT * FROM EMPLOYEE WHERE idNumber = (?)", (cashier,))
        
        if c.fetchone():
            break
        else:
            print('Employee doesn\'t exist')
    conn.commit()
    conn.close()
    return cashier