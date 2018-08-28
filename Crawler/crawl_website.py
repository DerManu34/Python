from Crawler import Crawler

myCrawler = Crawler()
if __name__ == "__main__":
	startUrl = "https://de.wikipedia.org/wiki/H%C3%B6he"
	print(startUrl)
	myCrawler.parseLinks(startUrl)



