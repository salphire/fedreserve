import scrapy
from scrapy.selector import Selector
from fedreserve.items import FedreserveItem
from scrapy.loader.processors import MapCompose
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor



class MySpider(scrapy.Spider):
  name = "spider"
  allowed_domains = [""]
  start_urls = ["https://www.federalreserve.gov/releases/h10/hist/dat00_al.htm"]
  """
  rules = (	Rule (LxmlLinkExtractor(allow=(),restrict_xpaths=('//a[@title="Go to forum"]',))
    , callback="parse_items", follow= True),
			Rule (LxmlLinkExtractor(allow=(),restrict_xpaths=('//a[@title="Next page"]',))
    , callback="parse_items", follow= True),
    )
  """
  
  
  
  
  def parse(self, response):
    hxs = response.xpath
    title = hxs('//tr[th[@headers="a1"]]')
    items = []
    for title in title:
      item = FedreserveItem()
      item ['Country'] = "Australia"
      item ['Monetary_Unit'] = "Dollars"
      item ['Date'] = title.select('th[@headers="a1"]/text()').extract()
      item ['Rate'] = MapCompose(unicode.strip)(title.select('td[@headers="a2 a1 r1"]/text()').extract())
      items.append(item)
    return items