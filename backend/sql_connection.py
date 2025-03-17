import mysql.connector

__cnx = None  #create a global variable to store the connection

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Aa2155033#',
                                        host='127.0.0.1',
                                        database='grocery_store')   #connect the database
    return __cnx