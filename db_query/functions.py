#File Name: functions.py
#Date: 2021-03-24
#Stores the functions for RUD - Read, Update and Delete
#Also has the functions for clear and press button to continue

import sqlite3
from os import system, name 
from . import error

def search(table, searchBy, t, s):
    '''Searches for an item in any table through user input
    Parameters:
    table- name of table
    searchBy - name of column
    t - type of variable
    s - user input prompt
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()

    if searchBy == 'position':
        searchItem = error.getPosition(s)
    elif searchBy == 'hireDate':
        searchItem = error.getDate(s)
    elif searchBy == 'dateTime':
        searchItem = error.getDateTime(s)
    elif searchBy == 'phoneNumber':
        searchItem = error.getPhone(s)
    elif t == 'float':
        searchItem = error.getFloat(s)
    elif t == 'int':
        searchItem = error.getInt(s)
    else:
        searchItem = input(s)

    c.execute(f"SELECT rowID, * FROM {table} WHERE {searchBy} = (?)", (searchItem,))
    if c.fetchone():
        c.execute(f"SELECT rowID, * FROM {table} WHERE {searchBy} = (?)", (searchItem,))
        items = c.fetchall()
    else:
        items = 'Doesn\'t exist'

    conn.commit()
    conn.close()

    return items

def getModifySearch(searchBy, searchT,s):
    '''gets the item which the user inputs
    to identify the row to modify
    Parameters:
    searchBy - column name
    searchT - item type
    s - prompt
    '''
    if searchBy == 'position':
        searchItem = error.getPosition(s)
    elif searchBy == 'hireDate':
        searchItem = error.getDate(s)
    elif searchBy == 'dateTime':
        searchItem = error.getDateTime(s)
    elif searchBy == 'phoneNumber':
        searchItem = error.getPhone(s)
    elif searchT == 'float':
        searchItem = error.getFloat(s)
    elif searchT == 'int':
        searchItem = error.getInt(s)
    else:
        searchItem = input(s)
    
    return searchItem

def modify(table, searchBy, modifyVar, searchT, modifyT, s, s1):
    '''Modifies an item in any table through user input
    Parameters:
    table- name of table
    searchBy - name of column that searches for row
    modifyVar - name of the column that will be modified
    searchT - type of variable that will be searched
    modifyT - type of variable that will be modified
    s - user input prompt for searching
    s1 - user input prompt for modifying
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()

    searchItem = getModifySearch(searchBy, searchT, s)
    
    if modifyVar == 'position':
        newItem = error.getPosition(s1)
    elif modifyVar == 'hireDate':
        newItem = error.getDate(s1)
    elif modifyVar == 'dateTime':
        newItem = error.getDateTime(s1)
    elif modifyVar == 'phoneNumber':
        newItem = error.getPhone(s1)
    elif modifyVar == 'itemSerialNumber' or modifyVar == 'idNumber':
        newItem = error.getID(table,modifyVar,s1)
    elif modifyT == 'float':
        newItem = error.getFloat(s1)
    elif modifyT == 'int':
        newItem = error.getInt(s1)
    else:
        newItem = input(s1)

    if modifyT != 'string':
        c.execute(f"UPDATE {table} SET {modifyVar} = {newItem} WHERE {searchBy} = (?)", (searchItem,))
    else:
        c.execute(f"UPDATE {table} SET {modifyVar} = '{newItem}' WHERE {searchBy} = (?)", (searchItem,))


    conn.commit()
    conn.close()

    print("Modification successfull")

def remove(table, searchBy, t, s):
    '''Removes for an row in any table through user input
    Parameters:
    table- name of table
    searchBy - name of column
    t - type of variable
    s - user input prompt
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()
    
    if searchBy == 'position':
        searchItem = error.getPosition(s)
    elif searchBy == 'hireDate':
        searchItem = error.getDate(s)
    elif searchBy == 'dateTime':
        searchItem = error.getDateTime(s)
    elif searchBy == 'phoneNumber':
        searchItem = error.getPhone(s)
    elif t == 'float':
        searchItem = error.getFloat(s)
    elif t == 'int':
        searchItem = error.getInt(s)
    else:
        searchItem = input(s)
    
    c.execute(F"DELETE from {table} WHERE {searchBy} = (?)", (searchItem,))
    print('Remove successfull')

    conn.commit()
    conn.close()
    

def view(table, item, ascending):
    '''Views the table through a certain order
    Parameters:
    table- name of table
    item - name of column that will be sorting by
    ascending - boolean for whether will be ascending or descending
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()
    if ascending:
        c.execute(f"SELECT rowId, * FROM {table} ORDER BY {item}")
    else:
        c.execute(f"SELECT rowId, * FROM {table} ORDER BY {item} DESC")

    items = c.fetchall()

    conn.commit()
    conn.close()

    return items

def viewRange(table,searchBy, larger,s):
    '''Views the table where a certain attribute is larger/smaller than or
    equal to an user input
    Parameters:
    table- name of table
    searchBy - column in table
    larger - boolean for whether will be ascending or descending
    s - prompt
    '''
    conn = sqlite3.connect('grocer.db')
    c = conn.cursor()
    if searchBy == 'stock':
        searchItem = error.getInt(s)
    else:
        searchItem = error.getFloat(s)
    
    if larger:
        c.execute(f"SELECT rowId, * FROM {table} WHERE {searchBy} >= {searchItem}")
    else:
        c.execute(f"SELECT rowId, * FROM {table} WHERE {searchBy} <= {searchItem}")

    items = c.fetchall()
    conn.commit()
    conn.close()

    return items

try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        '''Type any letter to continue
        '''
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

def clear():
    '''Clears the screen
    '''  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

def getchClear():
    getch()
    clear()
    