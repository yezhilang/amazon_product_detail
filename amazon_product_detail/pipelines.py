# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from amazon_product_detail.spiders.Dbmodels.productInfoModel import productInfo
from amazon_product_detail.spiders.Dbmodels.taskModel import taskModel

class AmazonProductDetailPipeline(object):
    def __init__(self):
        self.pd = productInfo()
        self.tm = taskModel()

    def process_item(self, item, spider):
        self.pd.insertIntoProductInfo(dict(item))
        self.tm.finishTask(dict(item)["asin"])
        # self.f.write(str(item)+"\r\n")
        return item
    def close_spider(self,spider):
        # self.f.close()
        pass
