from  mysql.connector import connect
import mysql.connector

db = connect(
    host = "sigma.jasoncoding.com",
    user = "alpha",
    passwd = "bestdatabase",
    database = "Books_n_Stationary",
    port =5555
)

def getdb():
    if not db.is_connected():
        db.reconnect()
    return db
    
def geterror():
    return mysql.connector.Error
