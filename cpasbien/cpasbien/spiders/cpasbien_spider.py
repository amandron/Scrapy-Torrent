from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from cpasbien.items import TorrentItem

class CpasbienSpider(Spider):

	name = "cpasbien"

	allowed_domains = [
	"cpasbien.pe"
	]
	start_urls = [
	'http://cpasbien.pe/recherche'
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		for entry in entries:
			item = TorrentItem()
			item['title'] = entry.select('td[1]/div[2]/a[2]/text()').extract()
			for s in self.keywords:
				if s.lower() in item['title'][0].lower():
					item['url'] = entry.select('td[1]/div[2]/a[2]/@href').extract()
					item['torrent'] = entry.select('td[1]/div[1]/a[starts-with(@title,"Download torrent file")]/@href').extract()
					item['size'] = entry.select('td[2]/text()[1]').extract()
					item['sizeType'] = entry.select('td[2]/span/text()').extract()
					item['age'] = entry.select('td[4]/text()').extract()
					item['seed'] = entry.select('td[5]/text()').extract()
					item['leech'] = entry.select('td[6]/text()').extract()	
					items.append(item)
					break	
		return items
