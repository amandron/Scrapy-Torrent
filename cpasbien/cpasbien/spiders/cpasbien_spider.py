from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.utils.response import get_base_url

from cpasbien.items import TorrentItem

class CpasbienSpider(Spider):

 name = "cpasbien"

 allowed_domains = [
  "cpasbien.pe"
 ]

 def __init__(self, *args, **kwargs):
  super(CpasbienSpider, self).__init__(**kwargs)
  self.keywords = kwargs['keywords']
  print self.keywords
  self.start_urls = [
   'http://cpasbien.pe/recherche/' 
    + self.keywords 
    + '.html'
  ]

def parse(self, response):
  sel = Selector(response)
  item = TorrentItem()
  item['name'] = sel.xpath("/div[@id='center-top']/href[1]/text()[2]").extract()
  item['description'] = sel.xpath("//div[@id='description']").extract()
  item['size'] = sel.xpath("//div[@id='informations-torrent']/strong[2]/text()      [2]").extract()
  item['url'] = sel.xpath("/div[@id=download-torrent']/href[1]/text()[2]").extract()
  return item
