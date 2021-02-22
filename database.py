'''
Created on 22 Feb 2021

@author: Anthony Bane
'''

import sqlite3
import pathlib
from IPython.core.history import sqlite3


class DATABASE(object):
    '''
    classdocs
    '''

    def __init__(self, location):
        '''
        Constructor
        '''

        self.databaseLocation = location

        self.db = self._getConnection(self.databaseLocation)

    def _getConnection(self, DB_location):
        db = sqlite3.connect(DB_location)
        return db

    # Function to acquire data from a database, returned as a Pandas dataframe
    def databaseGetData(self):
        pass

    # Function to store data into database
    def databaseStoreData(self):
        pass
