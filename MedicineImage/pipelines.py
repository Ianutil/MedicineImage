# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from scrapy.pipelines.images import ImagesPipeline
from MedicineImage import settings

class MedicineimagePipeline(object):
    def process_item(self, item, spider):
        url = item["url"]
        name = item["name"]
        print("process_item#", name, url)
        return item


# 下载图片分类
class MedicineimagePipeline(ImagesPipeline):

    # 这个方法是在发送下载请求之前调用的，其实这个方法本身就是去发送下载请求的
    def get_media_requests(self, item, info):
        request_objs = super(MedicineimagePipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    # 这个方法是在发送下载请求之前调用的，其实这个方法本身就是去发送下载请求的
    def file_path(self, request, response=None, info=None):
        path = super(MedicineimagePipeline, self).file_path(request, response, info)
        category = request.item.get('name')[0]
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

        image_name = path.replace('full/', '')

        image_path = os.path.join(category, image_name)
        # image_path = os.path.join(category_path, image_name)
        print("#############"+image_path)
        return image_path