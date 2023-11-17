# File Name: encryption.py
# Date: 2021-03-24
# This is the file that has the sign in to access program
# Makes sure users sign in with correct id and password

import sqlite3
import stdiomask #Importing this library is what is responsible for turning the text put into
#password into a *
import functions
import error

def signIn():
    """
    This function is will loop until it returns the position of the employee. It will do that
    once it firstly receives a valid username, then recieves a valid password. It first checks
    the table to ensure it makes sure the user ID exists in the table, once it does that, it 
    will ask for a password while masking it with *** to prevent snooping.
    """
    attempts = 5
    while True:
        attempts = attempts - 1
        conn = sqlite3.connect('grocer.db')
        c = conn.cursor()
        attempts = 5
        
        #Retrives user name and password from user
        username = error.getInt("ID: ")
        password = stdiomask.getpass(prompt= f"Password: ")
        c.execute("SELECT * FROM EMPLOYEE WHERE idNumber = (?)", (username,))

        #If statement makes sure username exists
        if c.fetchone():
            c.execute("SELECT * FROM EMPLOYEE WHERE idNumber = (?)", (username,))
            items = c.fetchall()

            #stores the Username, password, and the position of the user in variables to use later
            usernameCheck = items[0][5]
            passwordCheck = items[0][9]
            positionCheck = items[0][7]

            #If the password given and the password retrieve match, then go to the main menu
            if passwordCheck == password:
                print("Login Successful")
                print("Press any button to continue")
                functions.getchClear()
                return positionCheck

            # If the do not match, tell them to try again and restart the process 
            else:
                print("Wrong Password, Try Again")
                print('Type anything to continue')
                functions.getchClear()
        
        #If the username doesnt exist make them try again
        else:
            print("Username does not Exist")
            print('Type anything to continue')
            functions.getchClear()
