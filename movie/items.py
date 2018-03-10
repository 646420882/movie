# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    name = scrapy.Field()  # 电影名
    type = scrapy.Field()  # 电影类型
    url = scrapy.Field()

    image_urls = scrapy.Field()  # 图片地址
    images = scrapy.Field()  # 图片信息

    thunder = scrapy.Field()  # 迅雷下载
    qqdl = scrapy.Field()  # 旋风下载
    flashget = scrapy.Field()  # 快车下载
    ed2k = scrapy.Field()  # 电驴下载


