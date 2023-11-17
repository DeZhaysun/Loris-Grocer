# File Name: init_tables.py
# Date: 2021-03-24
# File Description: This file just initializes the database with the three tables in it


import sqlite3

conn = sqlite3.connect('grocer.db')
c = conn.cursor()
c.execute('''CREATE TABLE EMPLOYEE (
firstName TEXT NOT NULL,
lastName TEXT NOT NULL,
email TEXT NOT NULL,
phoneNumber INT NOT NULL,
idNumber INTEGER NOT NULL PRIMARY KEY,
salary REAL NOT NULL,
hireDate TEXT,
positionTitle TEXT NOT NULL,
reportTo TEXT, 
password TEXT NOT NULL
)''')
c.execute('''CREATE TABLE INVENTORY (
    itemName TEXT NOT NULL,
    itemSerialNumber INTEGER NOT NULL PRIMARY KEY,
    itemPrice FLOAT NOT NULL,
    itemDescription TEXT,
    stock INT NOT NULL
)''')
c.execute('''CREATE TABLE SALES (
    dateTime TEXT NOT NULL,
    product INT NOT NULL,
    employee INT NOT NULL,
    payment TEXT NOT NULL,
    nOfProducts INT NOT NULL,
    amountMade REAL NOT NULL,
    other TEXT
)''')
conn.commit()
conn.close()