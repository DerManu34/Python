#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from urllib.parse import urlparse

class Reader:

	def selectFromDbExecution(self, query, args):
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)
	 
			cursor = conn.cursor()
			cursor.execute(query, args)

	 		
			conn.commit()
		except Error as error:
			print(error)
	 
		finally:
			# cursor.close()
			conn.close()    
			return cursor

	def selectUrlToParse(self):
		query = "SELECT link FROM links WHERE parsed <= 0 limit 1"
		args = ()
		urlToParse = self.selectFromDbExecution(query, args)
		print(type(urlToParse))