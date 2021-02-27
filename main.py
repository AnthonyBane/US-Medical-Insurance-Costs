'''

This file contains the primary script for this project. A way for the user to access the underlying functionality.

Created on 22 Feb 2021

@author: Anthony Bane
'''

import database

if __name__ == '__main__':

    db = database.DATABASE('insurance-data.csv', True)
    df = db.databaseGetData()

    for row in df:
        print(row)
