# -*- coding: utf-8 -*-
import scrapy
from MedicineImage.items import MedicineimageItem
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 无头浏览器设置
chrome_options = Options()
chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')


class MedicineSpider(scrapy.Spider):
    name = 'Medicine'
    allowed_domains = ['111.com.cn']

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        super().__init__()

    header = {
        "User-Agent": "mozilla/5.0 (macintosh; intel mac os x 10_13_6) applewebkit/537.36 (khtml, like gecko) chrome/75.0.3770.142 safari/537.36"
    }

    # 初始URL
    start_urls = ["https://www.111.com.cn/",
                  "https://www.111.com.cn/search/search.action?keyWord=%25E5%25B8%2583%25E6%25B4%259B%25E8%258A%25AC%25E7%25BC%2593%25E9%2587%258A%25E8%2583%25B6%25E5%259B%258A(%25E8%258A%25AC%25E5%25BF%2585%25E5%25BE%2597)",
                  ]

    def start_requests(self):
        url = "https://news.163.com/"
        response = scrapy.Request(url, callback=self.parse_index)
        yield response

        # 整个爬虫结束后关闭浏览器

    def close(self, spider):
        self.browser.quit()

        # 访问主页的url, 拿到对应板块的response

    def parse_index(self, response):
        div_list = response.xpath("//div[@class='ns_area list']/ul/li/a/@href").extract()
        index_list = [3, 4, 6, 7]
        for index in index_list:
            response = scrapy.Request(div_list[index], callback=self.parse_detail)
            yield response

            # 对每一个板块进行详细访问并解析, 获取板块内的每条新闻的url

    def parse_detail(self, response):
        div_res = response.xpath("//div[@class='data_row news_article clearfix ']")
        # print(len(div_res))
        title = div_res.xpath(".//div[@class='news_title']/h3/a/text()").extract_first()
        pic_url = div_res.xpath("./a/img/@src").extract_first()
        detail_url = div_res.xpath("//div[@class='news_title']/h3/a/@href").extract_first()
        infos = div_res.xpath(".//div[@class='news_tag//text()']").extract()
        info_list = []
        for info in infos:
            info = info.strip()
            info_list.append(info)
        info_str = "".join(info_list)
        item = MedicineimageItem()

        item["name"] = title
        item["url"] = detail_url
        item["image_url"] = pic_url
        item["desc"] = info_str

        yield scrapy.Request(url=detail_url, callback=self.parse_content,
                             meta={"item": item})  # 通过 参数meta 可以将item参数传递进 callback回调函数,再由 response.meta[...]取出来

        # 对每条新闻的url进行访问, 并解析

    def parse_content(self, response):
        item = response.meta["item"]  # 获取从response回调函数由meta传过来的 item 值
        content_list = response.xpath("//div[@class='post_text']/p/text()").extract()
        content = "".join(content_list)
        item["content"] = content
        yield item

    def parse(self, response):
        # pass

        time.sleep(2)
        search_div = response.xpath('//div[@class="searchForm"]')
        print("div----------->", search_div)

        key = search_div.xpath('//label[@class="combobox-placeholder"]').extract_first()
        print("label----------->", key)
        button = search_div.xpath('//button[@class="searchBtn"]').extract()
        print("button----------->", button)

        # for label in data:
        #     text = label.xpath(".//text()").extract()
        #     print(text)
