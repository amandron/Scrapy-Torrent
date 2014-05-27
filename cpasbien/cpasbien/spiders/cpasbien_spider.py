from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from cpasbien.items import TorrentItem

class CpasbienSpider(BaseSpider):

 name = "cpasbien"

 allowed_domains = [
  "cpasbien.pe"
 ]

 def __init__(self, *args, **kwargs): 
  super(CpasbienSpider, self).__init__(**kwargs)
  self.keywords = kwargs['keywords'].split(',')
  self.start_urls = [
   'http://cpasbien.pe/recherche']

 def parse(self, response):
  items = []
  for entry in entries:
    item = TorrentItem()
    item['name'] = entry.select("/div[@id='center-top']/href[1]/text()[2]").extract()
    item['description'] = entry.select("//div[@id='description']").extract()
    item['size'] = entry.select("//div[@id='informations-torrent']/strong[2]/text()[2]").extract()
    item['url'] = entry.select("/div[@id=download-torrent']/href[1]/text()[2]").extract()
    for s in self.keywords:
     if s.lower() in item['title'][0].lower():
      items.append(item)
      break
  return items