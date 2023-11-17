#File Name: error.py
#Date: 2021-03-24
#Has all the functions that checks for errors

import sqlite3
def getFloat(s):
    '''Gets a float input based on prompt
    s - prompt
    '''
    num = False
    while num != True:
        try:
            amount = float(input(s))
        except:
            print("\nIncorrect input, please enter a float(a decimal number).")
        else:
            return amount

def getInt(s):
    '''Gets a integer input based on prompt
    s - prompt
    '''
    num = False
    while num != True:
        try:
            amount = int(input(s))
        except:
            print("\nIncorrect input, please enter a integer.")
        else:
            return amount

def getPosition(s):
    '''Gets employee position with a prompt
    s - prompt
    '''
    position = False
    realPositions = ['owner','supervisor','cashier']
    while position != True:
        p = input(s).lower()
        if p in realPositions:
            return p
        else:
            print('')

def getPhone(s):
    '''Gets a 10 digit phone number
    s - prompt'''
    phone = False
    while phone != True:
        number = getInt(s)
        if len(str(number)) != 10:
            print('Phone number must be 10 digits, no dashes')
        else:
            return number

def getDate(s):
    '''Gets date according to format YYYY-MM-DD
    s - prompt'''
    dateFormat = False
    number = ['0','1','2','3','4','5','6','7','8','9']
    while dateFormat != True:
        d = input(s)
        if len(d) != 10:
            print('Date has to be 10 digits. Follow formatting YYYY-MM-DD')
        else:
            good = True
            for i in range(10):
                if i == 4 or i == 7:
                    if d[i] != '-':
                        print('Follow formatting YYYY-MM-DD')
                        good = False
                        break            
                else:
                    if d[i] not in number:
                        print('Follow formatting YYYY-MM-DD')
                        good = False
                        break
            if good:
                return d

def getDateTime(s):
    '''Gets date according to format YYYY-MM-DD HH:MM
    s - prompt'''
    dateTimeFormat = False
    number = ['0','1','2','3','4','5','6','7','8','9']
    while dateTimeFormat != True:
        d = input(s)
        if len(d) != 16:
            print('Date and time has to be 16 digits. Follow formatting YYYY-MM-DD HH:MM')
        else:
            good = True
            for i in range(16):
                if i == 4 or i == 7:
                    if d[i] != '-':
                        print('Follow formatting YYYY-MM-DD HH:MM')
                        good = False
                        break
                elif i == 13:
                   if d[i] != ':':
                        print('Follow formatting YYYY-MM-DD HH:MM')
                        good = False
                        break
                elif i == 10:
                    if d[i] != ' ':
                        print('Follow formatting YYYY-MM-DD HH:MM')
                        good = False
                        break         
                else:
                    if d[i] not in number:
                        print('Follow formatting YYYY-MM-DD HH:MM')
                        good = False
                        break
            if good:
                return d

def getID(table,searchBy,s):
    '''Gets ID and makes sure there is no duplicate
    already in the database
    parameters:
    table - name of table
    searchBy - column in table
    s - prompt
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()
    while True:
        id = getInt(s)
        c.execute(f"SELECT * FROM {table} WHERE {searchBy} = (?)", (id,))
        
        if c.fetchone():
            print('ID already exists')
        else:
            conn.commit()
            conn.close()
            return id

