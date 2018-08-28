from lxml import html
import csv
import os
import requests
from time import sleep, time
from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup
from writer import Writer
from datetime import datetime

class Crawler:

	def __init__(self):
		pass



	def parseLinks(self, url):
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
		}
		
		try:
			# Retrying for failed requests
			for i in range(20):
				response = requests.get(url, headers=headers, verify=False)

				if response.status_code == 200: 
					doc = html.fromstring(response.content)

					XPATH_NAME = '//a/@href'
					RAW_NAME = doc.xpath(XPATH_NAME)
					if RAW_NAME:
						writer = Writer()
						for link in RAW_NAME:
							ts = time()
							timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')						
							writer.insert_link(link, url, timestamp)
							# return

				
				elif response.status_code==404:
					break

		except Exception as e:
			print (e)

	def parseBody(self, url):
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
		}
		
		try:
			# Retrying for failed requests
			for i in range(20):
				response = requests.get(url, headers=headers, verify=False)

				if response.status_code == 200: 
					doc = html.fromstring(response.content)

					XPATH_NAME = '//body//text()'
					RAW_NAME = doc.xpath(XPATH_NAME)
					BODY = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
					data =  BODY

					if data:
						ts = time()
						timestamp = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')		
						writer = Writer()		
						writer.insert_body(data, url, timestamp)
						return
				
				elif response.status_code==404:
					break

		except Exception as e:
			print (e)




