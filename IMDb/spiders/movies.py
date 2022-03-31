import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = "//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths = "(//div[@class='desc']/a)[2]"))
    )


    def parse_item(self, response):
      yield{

          "title" : response.xpath("//div[@class='sc-94726ce4-1 iNShGo']/h1/text()").get(),
          "year" : response.xpath("(//span[@class='sc-52284603-2 iTRONr'])[1]/text()").get(),
          "duration" : response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-52284603-0 blbaZJ baseAlt']/li[position()=last()]/text())[1]").get() + response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-52284603-0 blbaZJ baseAlt']/li[position()=last()]/text())[2]").get() + response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-52284603-0 blbaZJ baseAlt']/li[position()=last()]/text())[3]").get() + response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-52284603-0 blbaZJ baseAlt']/li[position()=last()]/text())[4]").get() + response.xpath("(//ul[@class='ipc-inline-list ipc-inline-list--show-dividers sc-52284603-0 blbaZJ baseAlt']/li[position()=last()]/text())[5]").get() ,
          "genre" : response.xpath("//div[@class='ipc-chip-list sc-16ede01-4 bMBIRz']/a/span/text()").get(),
          "rating" : response.xpath("(//span[@class='sc-7ab21ed2-1 jGRxWM'])[2]/text()").get(),
          "movie_url" : response.url
      }


