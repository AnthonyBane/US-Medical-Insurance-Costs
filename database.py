'''
Created on 22 Feb 2021

@author: Anthony Bane
'''

import sqlite3
import pandas as pd


class DATABASE(object):
    '''
    classdocs
    '''

    def __init__(self, location, create=False):
        '''
        Constructor
        '''

        self.databaseLocation = location
        self.db = None
        self.cursor = None

        if create == False:
            self.db = self._getConnection(self.databaseLocation)
        else:
            self._createDatabase(location)

    def _getConnection(self, DB_location):
        db = sqlite3.connect(DB_location)
        return db

    def _createDatabase(self, location):
        df = pd.read_csv(location)
        self.db = sqlite3.connect('insurance-data.db')
        self.cursor = self.db.cursor()
        df.to_sql(name='InsuranceData', con=self.db)
        return

    # Function to acquire data from a database, returned as a Pandas dataframe
    def databaseGetData(self):
        SQL_Query = pd.read_sql_query('''
            SELECT *
            FROM InsuranceData''', self.db
                                      )
        df = pd.DataFrame(SQL_Query, columns=[
                          'KEY', 'Age', 'Gender', 'BMI', 'Region', 'Charges'])
        return df

    # Function to store data into database
    def databaseStoreData(self):
        pass
