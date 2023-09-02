import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="")
    mycursor = mydb.cursor(buffered = True)
    print("Connection established successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    
def FExecution(filename):
    wh = open(filename,'r')
    mycursor.execute(wh.read())
    wh.close()

    