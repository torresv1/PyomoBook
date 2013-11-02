import pyodbc
connection = pyodbc.connect ( "DRIVER={PostgreSQL Unicode(x64)};SERVER=localhost;DATABASE=04_portofolio_data;UID=postgres;PWD=Caminero1" )
cursor = connection.cursor()
cursor.execute( "SELECT fund, asset_class, rank from rankings" )
for row in cursor:
    print row.fund, row.asset_class, row.rank
