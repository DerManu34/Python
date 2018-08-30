#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from urllib.parse import urlparse

class Reader:

	def selectFromDbExecution(self, query, args, fetchOne=False):
		try:
			db_config = read_db_config()
			conn = MySQLConnection(**db_config)
	 
			cursor = conn.cursor(buffered=True)
			cursor.execute(query, args)

	 		
			conn.commit()
		except Error as error:
			print(error)
	 
		finally:
			if(fetchOne):
				return cursor.fetchone()
			else:
				return cursor.fetchall()
			cursor.close()
			conn.close()    

	def selectUrlToParse(self):
		query = "SELECT link FROM links WHERE parsed <= 0 limit 1"
		args = ()
		urlToParse = self.selectFromDbExecution(query, args, True)
		urlToParse = urlToParse[0]
		return urlToParse

	def selectOpenUrlsToParse(self):
		query = "SELECT link FROM links WHERE parsed <= 0 limit 100"
		args = ()
		urlToParse = self.selectFromDbExecution(query, args, False)
		urlToParse = urlToParse
		return urlToParse