# -*- coding: utf-8 -*-
import scrapy
from MedicineImage.items import MedicineimageItem


class NetbianimagedownloadSpider(scrapy.Spider):
    name = 'NetBianImageDownload'
    allowed_domains = ['pic.netbian.com']
    # start_urls = ['http://pic.netbian.com/']
    start_urls = ["http://pic.netbian.com/4kmeinv/"]

    def parse(self, response):
        # pass
        picture_list = response.xpath('//ul[@class="clearfix"]/li/a//@src').extract()
        for pic in picture_list:
            url = 'http://pic.netbian.com/' + pic
            print("----------->", url)
            item = MedicineimageItem()
            item['url'] = [url]
            yield item

            next_pages = response.xpath('//div[@class="page"]/a/@href').extract()

            # 进入下一页
            for page in next_pages:
                # 判断是否拿到值
                if len(page) != 0:
                    page_url = 'http://pic.netbian.com/'+page
                    print("下一页", page_url)
                    yield scrapy.Request(url=page_url, callback=self.parse)