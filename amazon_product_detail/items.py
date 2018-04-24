# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonProductDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    asin = scrapy.Field()
    bestSellerRank = scrapy.Field()
    category = scrapy.Field()
    sprddetail2 = scrapy.Field()
    sprddetail1 = scrapy.Field()
    customsAlsoView = scrapy.Field()
    frequentlyBought = scrapy.Field()
    price = scrapy.Field()
    stars_reviews = scrapy.Field()
    compareSimilarProducts = scrapy.Field()
    customsAlsoBought = scrapy.Field()
    time = scrapy.Field()
