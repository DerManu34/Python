from lxml import html
import csv
import os
import requests
from time import  time
from writer import Writer
from reader import Reader
from datetime import datetime

class Crawler:

	def __init__(self):
		pass

	def parseUrl(self, url, xpath, type):
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
		}
		try:
			# Retrying for failed requests
			for i in range(20):
				response = requests.get(url, headers=headers, verify=False)

				if response.status_code == 200: 
					doc = html.fromstring(response.content)
					XPATH_NAME = xpath
					RAW_NAME = doc.xpath(XPATH_NAME)
					if type == 'body':
						print("\r\n")
						print('doin body')
						LANGUAGE = doc.xpath('//html/@lang')
						LANGUAGE = LANGUAGE[0]
						BODY = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
						data =  BODY
						writer = Writer()			
						ts = time()
						timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
						if data and LANGUAGE == 'de':
							writer.insertBody(data, url, timestamp)
						# print('weiter')
						# print(url)
						# # print(type(url))
						# print(timestamp)
						# # print(type(timestamp))
						# print(LANGUAGE)
						# print(type(LANGUAGE))
						writer.updateLink(url, timestamp, LANGUAGE)
					elif type == 'links':
						print('doin links')
						print("\r\n")
						if RAW_NAME:
							writer = Writer()
							for link in RAW_NAME:
								ts = time()
								timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')						
								writer.insertLink(link, url, timestamp)
					break
				elif response.status_code==404:
					print('got status code 404')
					break

		except Exception as e:
			print (e)


	def getUrlToParse(self):
		reader = Reader()
		urlToParse = reader.selectUrlToParse()
		return urlToParse

	def getOpenUrlsToParse(self):
		reader = Reader()
		openUrlsToParse = reader.selectOpenUrlsToParse()
		return openUrlsToParse


	def runLoop(self, limit, end):
		linklist = self.getOpenUrlsToParse()
		if end == 0:
			return		
		for index, link in enumerate(linklist):
			link = link[0]
			print(link)


			self.parseUrl(link, '//a/@href', 'links')
			self.parseUrl(link, '//body//text()', 'body')	

			if index == end:
				return
			if index == limit:
				print("\r\n")
				newEnd = end - index
				self.runLoop(limit, newEnd)

