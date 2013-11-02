# Name:      Challenge 2 of MIT System Optimization Course
# Purpose:    Portfolio optimization - Finding the optimal asset allocation across different funds.
# Date:       10/31/2013 1:19 PM
# Author:     Vladimir Torres-Rivas

#-------------------------------------------------------------------------------------------------

# Python import statement

from coopr.pyomo import *
import pyodbc

#-------------------------------------------------------------------------------------------------

# Create a Pyomo model object

model = AbstractModel()


# Define model set and parameters

model.fund = Set()
model.asset_class = Set()
model.rank = Param( model.fund, model.asset_class )

# Connect to the Portfolio database

connection = pyodbc.connect( "DRIVER={psqlOBDC};SERVER=localhost;DATABASE=04_portofolio_data;UID=postgres;PWD=Caminero1" );



# connection = pyodbc.connect("DRIVER={psqlOBDC};SERVER=localhost;DATABASE=04_portofolio;UID=postgres;PWD=Caminero1");

