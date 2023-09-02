import pysql as ps
mycursor = ps.mycursor
mydb = ps.mydb

mycursor.execute("CREATE DATABASE IF NOT EXISTS pysql_db;")
mycursor.execute('use pysql_db;')
print("Database has been created")

# Warehose table creation 
ps.FExecution('Warehose_tb.sql')

# Boxes table creation 
ps.FExecution('Boxes_tb.sql')
print("Tables have been created")

#insert warehouse data 
ps.FExecution('wdata.sql')

#insert boxes data 
ps.FExecution('bdata.sql')
print("Successfully Data inserted into Tables")

mydb.commit()

print("Completed")
