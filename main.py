#!/usr/bin/python
# -*- coding: UTF-8 
# author: Ian
# Please,you must believe yourself who can do it beautifully !
"""
Are you OK?
"""
from scrapy.cmdline import execute

if __name__ == "__main__":

    # execute("scrapy crawl ImageDownload -o baidu_image.csv".split())  # 用命令行启动
    # execute(['scrapy', 'crawl', 'Medicine-YaoFang'])
    # execute(['scrapy', 'crawl', 'Medicine'])
    # execute(['scrapy', 'crawl', 'NetBianImageDownload'])
    # execute("scrapy crawl NetBianImageDownload -o net_bian_image.csv".split())  # 用命令行启动
    # execute(['scrapy', 'crawl', 'Medicine-JD'])
    execute(['scrapy', 'crawl', 'Medicine_YAOPIN'])

    # print(isinstance([], list))
