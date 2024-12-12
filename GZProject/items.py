# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GzprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()          # 品种名称
    price_type = scrapy.Field()          # 价格类型
    price = scrapy.Field()          # 价格
    unit = scrapy.Field()          # 单位
    market_name = scrapy.Field()          # 市场名称
    time = scrapy.Field()          # 发布时间
