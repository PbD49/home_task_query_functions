from create_table_query import create_db
from select_query import find_client
from insert_query import add_client, add_phone
from delete_query import delete_client, delete_phone
from update_query import change_client
import configparser
import psycopg2


config = configparser.ConfigParser()
config.read("settings.ini")


if __name__ == '__main__':
    username = config["name"]["username"]
    password = config["password"]["password"]
    connection = psycopg2.connect(dbname='clients', user='postgres', password='5814', host='127.0.0.1', port='5432')
    cursor = connection.cursor()

    create_db(cursor)

    add_client(cursor, "Ньют", "Саламандр", "ivan@example.com", [123456789, 987654321])
    add_client(cursor, "Петр", "Петров", "petr@example.com", [111222333])

    add_phone(cursor, 23, 999888777)

    change_client(cursor, 23, first_name="Ньют")

    delete_phone(cursor, 23, 987654321)
    delete_client(cursor, 6)

    print(find_client(cursor, first_name="Ньют", last_name=None, email=None, phone=None))

    connection.commit()
    cursor.close()
    connection.close()
