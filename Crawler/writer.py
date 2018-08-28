from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_body(body, url, timestamp):
    query = "INSERT INTO bodies(body,url,`timestamp`) " \
            "VALUES(%s,%s, %s)"
    args = (body, url, timestamp)
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.execute(query, args)
 
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
# def main():
#    insert_book('A Sudden Light','9781439187036')
 
# if __name__ == '__main__':
#     main()
