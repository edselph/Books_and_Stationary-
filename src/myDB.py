import mysql.connector
from mysql.connector import connect

db = connect(
  host = "sigma.jasoncoding.com",
  user = "alpha",
  password = "bestdatabase",
  database = "Books_n_Stationary",      
  port = 5555
)

def getDb():
    if not db.is_connected():
        db.reconnect()
    return db

def getDbError():
    return mysql.connector.Error