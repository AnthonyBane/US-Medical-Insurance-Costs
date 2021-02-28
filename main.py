'''

This file contains the primary script for this project. A way for the user to access the underlying functionality.

Created on 22 Feb 2021

@author: Anthony Bane
'''

import database

if __name__ == '__main__':

    # A simple way to create the database from a csv file
    # Future improvements would be to take a string from the user
    # and whether to create a new database to overwrite the previous one if it
    # exists
    db = database.DATABASE('insurance-data.csv', True)
    df = db.databaseGetData()

    for row in df:
        print(row)
