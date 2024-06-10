import mysql.connector
from mysql.connector import Error


def connect_database():
    """  Connect to the MySQL database and return the connection object """
    db_name = "e_commerce_db"
    user = "root"
    #Add your password
    password = "Mario101299"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        print("Connected to MySQL database successfully")
        return conn

    
    except Error as e:
        print(f"Error: {e}")
        return None