import mysql.connector
from mysql.connector import Error, connect
from mysql.connector import connection
from setup import database

def create_connection(host_name, port, user_name, user_password, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port=port,
            user=user_name,
            passwd=user_password,
            database=db
        )
        print("Connection to MYSQL DB Successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def insert_member(data):
    connection = create_connection(host_name=database['host'],
                                port=database['port'], 
                                user_name=database['user'], 
                                user_password=database['passwd'], 
                                db=database['database'])

    cursor = connection.cursor()
    
    add_member = (
        "INSERT INTO MEMBRO"
        "(CPF_Membro, Nome, Tipo_Quarto, Estado_Presenca)"
        "VALUES (%s,%s,%s,%s)"
    )

    cursor.execute(add_member, data)

    connection.commit()

    cursor.close()
    connection.close()