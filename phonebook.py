from sys import argv
import sqlite3
from cs50 import get_string


# Checking if correct number of command line arguments are input

if len(argv) != 1:
    print("Usage: python phonebook.py")
    exit(1)
# Connect with .db file and make cursor
con = sqlite3.connect('contact.db')
cur = con.cursor()
person = get_string("Enter the persons full name:")

# Query the database for persons details
cur.execute('SELECT * FROM name WHERE name = "{}";'.format(person))
phonebook = cur.fetchall()

# Check if the person exists in the database
if len(phonebook) == 0:
          print("No data available about the person you requested")

# Iterate through each row to print the persons details
for row in phonebook:
    print("Name: {}\nNumber: {}\nEmail: {}".format(row[0],row[1],row[2]))
con.close()







