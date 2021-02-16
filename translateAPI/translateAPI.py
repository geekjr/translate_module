import mysql.connector
import requests


def mysql(url, username, password, table):
    """
            This method is for translating MySQL databases
            :param url: Connection url to database
            :param username: Your username for the database
            :param password: Your password for the database
            :param table: The table you want to translate
            :return: Returns query that you can insert into MySQL table
            """
    db = mysql.connector.connect(
        host=url,
        user=username,
        password=password,
    )
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    columns_cursor = cursor.fetchall()
    columns = []
    for column in columns_cursor:
        columns.append(column[0])
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    translated_final = {}
    for x in result:
        column_id = 0
        for y in x:
            translated_final.update({columns[column_id]: y})
            column_id += 1
    print(translated_final)
    url = 'http://52.152.216.112/json'
    data = {'text': translated_final}
    x = requests.post(url, data=data)

    print(x.text)

def postgres():
    ffg

