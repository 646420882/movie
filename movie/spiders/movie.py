import scrapy
from scrapy import Request
from movie.items import MovieItem

class movie(scrapy.Spider):
    index = 'https://777av.vip'
    name = 'movie'
    #allowed_domains = [index]
    start_urls = ['https://777av.vip/']
    page = 15000
    # rules = (
    #     Rule(LinkExtractor(allow=('https://777av.vip/vod/\d{1,5}.html')),
    #          callback='parse_item', follow=True),
    # )
    def start_requests(self):
        for i in range(1, self.page):
            url = 'https://777av.vip/vod/' + str(i) + '.html'
            yield Request(url, callback=self.parse_item)


    def parse_item(self,response):
        item = MovieItem()
        name = response.xpath('//div[@id="main"]//div[@class="info"]/h1/text()').extract_first()
        type = response.xpath('//div[@id="main"]//div[@class="info"]/ul/li[1]/a/@title').extract_first()
        url = response.url
        image_urls = []
        images = response.xpath('//div[@class="endtext vodimg"]/p/img/@src').extract()
        for img in images:
            if 'http' not in img:
                img = 'http:' + img
            image_urls.append(img)
        thunder = response.xpath('//div[@class="downlist"]/ul/li/span/a[@class="d1"]/@href').extract_first()
        qqdl = response.xpath('//div[@class="downlist"]/ul/li/span/a[@class="d2"]/@href').extract_first()
        flashget = response.xpath('//div[@class="downlist"]/ul/li/span/a[@class="d3"]/@href').extract_first()
        ed2k = response.xpath('//div[@class="downlist"]/ul/li/span/a[@class="d4"]/@href').extract_first()

        item['name'] = name
        item['type'] = type
        item['url'] = url
        item['image_urls'] = image_urls
        item['thunder'] = thunder
        item['qqdl'] = qqdl
        item['flashget'] = flashget
        item['ed2k'] = ed2k
        yield item



