import configparser
import mysql.connector
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def get_user():
    authenticator = 'rahulshettyacademy'
    return authenticator


def get_password():
    password = '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'
    return password


connection_config = {
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database'],
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password']
}


def get_connection():
    try:
        connection = mysql.connector.connect(**connection_config)
        if connection.is_connected():
            print(f'Connection with database {connection_config["database"]} is established successfully.')
            return connection
    except Error as e:
        print(e)


def get_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    connection.close()
    return row
