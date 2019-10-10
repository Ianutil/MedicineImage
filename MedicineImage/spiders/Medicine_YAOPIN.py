# -*- coding: utf-8 -*-
import scrapy
from MedicineImage.items import MedicineimageItem

class MedicineYaopinSpider(scrapy.Spider):
    name = 'Medicine_YAOPIN'
    allowed_domains = ['yao.xywy.com']
    start_urls = [
        'http://yao.xywy.com/',
        "http://yao.xywy.com/search/?q=%E5%90%89%E6%9E%97%E9%91%AB%E8%BE%89+%E7%89%9B%E9%BB%84%E8%A7%A3%E6%AF%92%E7%89%87&sort=complex&pricefilter=0"]

    header = {
        "User-Agent": "mozilla/5.0 (macintosh; intel mac os x 10_13_6) applewebkit/537.36 (khtml, like gecko) chrome/75.0.3770.142 safari/537.36"
    }

    def parse(self, response):
        # pass
        # div_list = response.xpath('//div[@class="h-drugs-item"]')
        div_list = response.xpath('//div[@class="fl h-drugs-pic bor"]')
        print(div_list)

        detail_list = div_list.xpath('//a//@href').extract()
        picture_list = div_list.xpath("//img//@src").extract()
        name_list = response.xpath("//img//@alt").extract()

        detail_urls = []
        # for pic in picture_list:
        for i in range(0, len(picture_list)):
            detail_url = detail_list[i]
            pic_url = picture_list[i]
            name = name_list[i]
            detail_urls.append(detail_urls)
            print("----------->", pic_url, detail_url, name)
            # item = MedicineimageItem()
            # item['url'] = [pic_url]
            # item['name'] = [name]
            # yield item

        for pic in detail_list:
            # url = "http:"+pic[2:]
            # url = "http://yao.xywy.com"+pic
            url = pic
            print("----------->", url)
            yield scrapy.Request(url=url, callback=self.parse)
