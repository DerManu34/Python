from Crawler import Crawler

myCrawler = Crawler()
if __name__ == "__main__":

	returnURLsToParse = myCrawler.getOpenUrlsToParse()
	# print(returnURLsToParse)
	myCrawler.runLoop(limit=20, end=30)
	# limit = 5
	# for index, link in enumerate(returnURLsToParse):
	# 	print(link[0])
	# 	if index == limit:
	# 		break

	# startUrl = "https://de.wikipedia.org/wiki/H%C3%B6he"
	# myCrawler.parseUrl(startUrl, '//a/@href', 'links')
	# myCrawler.parseUrl(returnToParse, '//body//text()', 'body')	



