import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc/']

# FAILED ATTEMPT USER AGENT MODIFICATION 

    # user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"

    # def start_request(self):
    #     yield scrapy.Request(url='https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc/', headers={
    #         'User-Agent' : self.user_agent
    #     })

    rules = (
        Rule(LinkExtractor(restrict_xpaths = "//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths = "(//div[@class='desc']/a)[2]"))
    )


# fAILED ATTEMPT USER AGENT MODIFICATION 

    # def set_user_agent(self,request):
    #     request.headers['User-Agent'] = self.user_agent
    #     return request



    def parse_item(self, response):
      yield{

          "title" : response.xpath("//div[@class='sc-94726ce4-1 iNShGo']/h1/text()").get(),
          "year" : response.xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div/ul/li[1]/span/text()").get(),
          "duration" : "".join(response.xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/div/ul/li[3]/text()").getall()),
          "genre" : ",".join(response.xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/descendant::*/text()").getall()),
          "rating" : response.xpath("(//span[@class='sc-7ab21ed2-1 jGRxWM'])[2]/text()").get(),
          "movie_url" : response.url,
        #   "user-agent" : response.request.headers['User-Agent']
      }


