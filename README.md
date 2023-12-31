# Grocer Management System

## About: 
Tasked to make a database **Python** program that can do **CRUD** using SQLite3. 
- The system comprises three tables: inventory, employee, and sales
- Each table supporting CREATE, READ, UPDATE, and DELETE (CRUD) operations
- Employee roles include owner, supervisor, and cashier, with the owner having unrestricted access
- Passwords are concealed for security using `stdiomask`
- Comprehensive error checking is implemented for user inputs to maintain data integrity and enhance the user experience

![image](https://github.com/DeZhaysun/lorisgrocer/assets/61562373/4853026e-a3da-4073-a201-2c8265be7d82)
![image](https://github.com/DeZhaysun/lorisgrocer/assets/61562373/4566078b-afa7-4486-8f26-d1a396fc5538)
![image](https://github.com/DeZhaysun/lorisgrocer/assets/61562373/0c1c9e81-511a-47fc-9fb1-b7c1b2ecb338)

## Usage:
The database is initialized already, but run init_tables.py to create the tables in the database.

Run main.py

### Master Password:
ID: 1
Password: x

## How it works:
There are functions for every menu, and certain functions are stored in different files for superior organization.
Each menu either calls another sub-menu, or a function from the functions.py file, that will run one of the CRUD functions.
Before you can access the menu, there is a sign-in (file: encryption.py) where the program knows what position you have in 
order to restrict certain functions.
There are error-checking functions for inputs to ensure the program doesn't crash, and the user input is correct.
For a more in-depth user manual, check README.md

## Known errors and limitations:
The item name in inventories has to be lower case, when doing accessing, modifying, and removing.
The user cannot quit the program or go back once they've entered a non-menu function when they 
don't know the correct input.
Commas can possibly create problems in certain string inputs when doing a SQLite execution. This is extremely rare.

