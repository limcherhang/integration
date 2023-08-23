"""
    python3 example_connect_mysql.py
    Note: db_config.yaml must include your database config called mysql_own, do not use directly!
"""
import sys
sys.path.append('../connection')

from mysql_connection import MySQLConn

if __name__ == "__main__":
    
    connection = MySQLConn("own", dict_mode=False)

    with connection.cursor() as cursor:
        cursor.execute("SELECT (1+1) AS solution;")

        result = cursor.fetchall()

    print(result)

    connection.close()