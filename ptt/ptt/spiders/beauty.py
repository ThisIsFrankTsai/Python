from ptt.items import PostItem
import scrapy
import time

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Beauty/index.html']

    def parse(self, response):
        for i in range(10):
            time.sleep(1)
            url = "https://www.ptt.cc/bbs/Beauty/index" + str(3941 - i) + ".html"
            yield scrapy.Request(url, cookies={'over18':'1'}, callback=self.parse_article)

    def parse_article(self, response):
        item = PostItem()
        target = response.css("div.r-ent")

        for tag in target:
            try:
                item['title'] = tag.css("div.title a::text")[0].extract()
                item['author'] = tag.css('div.author::text')[0].extract()
                item['date'] = tag.css('div.date::text')[0].extract()
                item['push'] = tag.css('span::text')[0].extract()
                item['url'] = tag.css('div.title a::attr(href)')[0].extract()

                yield item

            except IndexError:
                pass
            continue
