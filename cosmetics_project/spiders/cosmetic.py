import scrapy 


class CosmeticSpider(scrapy.Spider):
    name = 'cosmetic'
    allowed_domains = ['goschonheit.ch']
    # start_urls = ['http://goschonheit.ch/']

    def start_requests(self):
        yield scrapy.Request('http://goschonheit.ch/', callback=self.parse_city)
    
    def parse_city(self, response):
        cities = response.xpath("//span[@class='li_inner']/a")
        for city in cities:
            yield response.follow(city.xpath('./@href').get()+'?distance=99999', callback=self.open_entity, meta={'city': city.xpath('./text()').get()})
            break
    def open_entity(self, response):
        for shop in response.xpath("//h3/a/@href").getall():
            # print('Shop: ', shop)
            yield response.follow(shop, callback=self.parse_entity, meta={'city': response.meta.get('city')})
            break
        nxt = response.xpath("//div[@class='pagination']/a[contains(., 'chste')]/@href").get()
        if nxt:
            yield response.follow(nxt, callback=self.open_entity, meta={'city': response.meta.get('city')})

    def parse_entity(self, response):
        out = {
            'name': response.xpath("//h1/text()").get(),
            'rating': response.xpath("(//span[@class='average'])[1]/text()").get(),
            'address': response.xpath("//div[@class='adr']/text()").getall(),
            'phone': response.xpath("//div[@itemprop='telephone']/text()").get(),
            'website': response.xpath("//div[@class='ca_content_info'][1]/div[last()]/text()").get(),
            'city': response.meta.get('city'),
        }
        # print(out)
        yield out

