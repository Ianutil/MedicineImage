# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MedicineimageItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()
    image_url = scrapy.Field()
    date = scrapy.Field()

    # 下载成功后返回有关images的一些相关信息
    images = scrapy.Field()
    pass
