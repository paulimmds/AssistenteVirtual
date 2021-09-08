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

def update_bill(data):
    connection = create_connection(host_name=database['host'],
                                port=database['port'], 
                                user_name=database['user'], 
                                user_password=database['passwd'], 
                                db=database['database'])

    
    cursor = connection.cursor()

    year, month = data[0].year, data[0].month

    query_check = ("SELECT * FROM CONTA WHERE year(Data_Referencia) = %s and month(Data_Referencia) = %s;")

    cursor.execute(query_check, (year, month))

    cursor.fetchall()

    if cursor.rowcount == 0:
        query = (
            "INSERT INTO CONTA "
            "(Data_Referencia, " + data[1] + ")"
            "VALUES (%s, %s);")

        cursor.execute(query, (data[0], data[2]))

    else :
        query = (
            "UPDATE CONTA "
            "SET " + data[1] + " = %s "
            "WHERE year(Data_Referencia)=%s and month(Data_Referencia)=%s")

        cursor.execute(query, (data[2], year, month))
    
    connection.commit()

    cursor.close()
    connection.close()

def insert_forms(data):
    connection = create_connection(host_name=database['host'],
                                port=database['port'], 
                                user_name=database['user'], 
                                user_password=database['passwd'], 
                                db=database['database'])
    
    cursor = connection.cursor()

    id_tipo = (f"SELECT (ID_Tipo) FROM (TIPO_FORMS) WHERE (Tipo) = '{data[1]}';")

    cursor.execute(id_tipo)

    cursor.fetchall()

    if cursor.rowcount == 0:
        query = (f"INSERT INTO TIPO_FORMS (Tipo) VALUES ('{data[1]}');")

        cursor.execute(query)

    month, year = data[2].month, data[2].year

    cursor.execute(id_tipo)
    id_tipo = cursor.fetchone()

    id_conta = ("SELECT (ID_Conta) from (CONTA) WHERE year(Data_Referencia)=%s and month(Data_Referencia)=%s")

    cursor.execute(id_conta, (year, month))
    
    id_conta = cursor.fetchone()

    query = (
        "INSERT INTO FORMS"
        "(CPF_Membro, ID_Tipo, ID_Conta, Valor, Data_Pagamento)"
        "VALUES (%s,%s,%s,%s,%s)"
    )

    data[1], data[2] = id_tipo[0], id_conta[0]

    cursor.execute(query, data)

    connection.commit()

    cursor.close()
    connection.close()
