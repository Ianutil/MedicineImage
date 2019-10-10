# -*- coding: utf-8 -*-
import scrapy
import json
from MedicineImage.items import MedicineimageItem

'''
从百度上面，爬下图片
'''
class ImagedownloadSpider(scrapy.Spider):
    name = 'ImageDownload'
    allowed_domains = ['image.baidu.com']
    start_urls = [
        'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%87%91%E6%9C%A8%E7%A0%94&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E9%87%91%E6%9C%A8%E7%A0%94&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&pn=30&rn=30&gsm=1e&1541678883249=',
        'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E9%87%91%E6%9C%A8%E7%A0%94&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%E9%87%91%E6%9C%A8%E7%A0%94&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&pn=60&rn=30&gsm=3c&1541678883388='
    ]

    def parse(self, response):
        # pass
        # 从Json文件内容中提取所有img的内容
        imgs = json.loads(response.body)['data']
        for eachImage in imgs:
            item = MedicineimageItem()  # items中的类
            try:
                item['image_url'] = [eachImage['middleURL']]
                item['name'] = [eachImage['fromPageTitleEnc']]
                item['date'] = [eachImage['bdImgnewsDate']]
                print(item["image_url"], item["name"], item["date"])

                yield item
            except Exception as e:
                print(e)

