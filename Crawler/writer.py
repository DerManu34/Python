#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from urllib.parse import urlparse

class Writer:

    def getCursor(self):
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        return cursor, conn

    def insertToDbExecution(self, query, args):
        try:
            cursor, conn = self.getCursor()
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

    def updateDbExecution(self, query, args):
        try:
            cursor, conn = self.getCursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as error:
            print(error)
     
        finally:
            cursor.close()
            conn.close()                    



    def insertBody(self, body, url, timestamp):
        query = "INSERT INTO bodies(body,url,`timestamp`) " \
                "VALUES(%s,%s,%s)"
        args = (body, url, timestamp)
        self.insertToDbExecution(query, args)




    def insertLink(self, link, origin, timestamp):
        linkWithoutEncoding = link.encode('utf8')
        link = link
        query = "INSERT INTO links(link,origin, `timestamp`) " \
                "VALUES(%s,%s,%s)"

        parsed_uri2 = urlparse(link)
        result2 = '{uri.netloc}'.format(uri=parsed_uri2)
  
        if not parsed_uri2.scheme:    
            parsed_uri = urlparse(origin)
            baseUrl = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            finalLink = baseUrl+str(link)
        else: 
            finalLink = linkWithoutEncoding


        args = (finalLink, origin, timestamp)

        self.insertToDbExecution(query, args)       

    def updateLink(self, link, timestamp, lang):
        query = "UPDATE links SET parsed=%s, lang=%s WHERE link=%s"
        args = (timestamp, lang.encode('utf8'), link)
        self.updateDbExecution(query, args)
 
