# coding:utf-8
import scrapy

from amazon_product_detail.items import AmazonProductDetailItem
from amazon_product_detail.spiders.Dbmodels.productInfoModel import productInfo
from .parser import parser
from amazon_product_detail.spiders.Dbmodels.taskModel import taskModel
import time


class productSpider(scrapy.Spider):
    name = "product"


    def getTasks(self):
        tasks = []

        for task in tasks:
            yield task

    def start_requests(self):
        # start_url = ["#"]
        base_url = "https://www.amazon.com/dp/"
        tasks = []
        tm = taskModel()

        tasks = tm.getTasks()
        for task in tasks:
            url = base_url + str(task)
            # # yield
            # print("-------------------------"+url+"-----------------")
            yield scrapy.Request(url, callback= self.parse,meta={"asin":task})




    def parse(self, response):

        p = parser(html=response.text,asin=response.meta["asin"])
        data = p.extractData()
        # print data
        pd = productInfo()
        item = NewamazonproductdetailItem()
        item["asin"] = response.meta["asin"]
        item["bestSellerRank"] = data["bestSellerRank"]
        item["category"] = data["category"]
        item["sprddetail2"] = data["sprddetail2"]
        item["sprddetail1"] = data["sprddetail1"]
        item["customsAlsoView"] = data["customsAlsoView"]
        item["frequentlyBought"] = data["frequentlyBought"]
        item["price"] = data["price"]
        item["stars_reviews"] = data["stars&reviews"]
        item["compareSimilarProducts"] = data["compareSimilarProducts"]
        item["customsAlsoBought"] = data["customsAlsoBought"]
        item["time"] = time.strftime("%Y-%m-%d %H:%M:%S")

        # pd.insertIntoProductInfo(data)
        # print "before print ------------------2312"
        # print item
        # print "after print______________--------------345"
        yield item















        # _item = {}
        #
        # try:
        #     price = response.xpath("//*[@id='priceblock_ourprice']/text()").extract()[0].strip()
        #
        #     _item["price"] = price
        # except IndexError:
        #     with open("temp.html","w+") as f:
        #         f.write((response.text).decode())
        #
        # category =  response.xpath("//*[@id='productTitle']/text()").extract()[0].strip()
        #
        # _item["category"] = category
        #
        # deliver_fee = response.xpath("//*[@id='ourprice_shippingmessage']/span/b/text()").extract()[0].strip()
        #
        # _item["deliver_fee"] = deliver_fee
        #
        # product_brief = {"item":[]}
        #
        #
        #
        # x = response.xpath("//*[@id='fbExpandableSectionContent']/ul/li")
        #
        # for i in x:
        #     item = i.xpath("./span[1]/text()").extract()[0].strip()
        #     product_brief["item"].append(item)
        # _item["product_brief"] = product_brief
        #
        # product_detail = {}
        #
        # x = response.xpath("//*[@id='detail-bullets']/table/tr/td/div/ul/li")
        # for i in x:
        #     _key = i.xpath("./b/text()").extract()[0].strip()
        #
        #     try:
        #         xpath = XPATH_RULE[_key[:-1]]
        #     except KeyError:
        #         with open("logger.txt","a+") as f:
        #             s = "\r\n" + "url:" + response.url + " -- key: " + str(_key) + " -- time: "+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        #             f.write(s)
        #         continue
        #     _value = response.xpath(xpath["parse_rule"]).extract()[0].strip() if xpath["parse_once"] else xpath["_value"](response.text)
        #
        #     product_detail[_key] = _value
        #
        # _item["product_detail"] = product_detail
        # # from lxml import etree
        # # a = response.xpath("//*[@id='SalesRank']").extract()[0]
        # # li = etree.HTML(a.replace("\n", "")).xpath("//li[@id='SalesRank']")
        # # # li.xpath("./text()")
        # # # li[0].xpath("./text()")
        # #
        # # salesrank = li[0].xpath("./text()")[0][:-1].strip()
        # #
        # # _item["salesrank"] = salesrank
        #
        # try:
        #     important_information = response.xpath("//*[@id='importantInformation']/div/div/text()")[1].extract()
        #     _item["important_information"] = important_information
        # except:
        #     pass
        #
        # with open("j.txt","a+") as f:
        #     for i in _item:
        #         f.writelines(str(i+":"+str(_item[i])+"   "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))+"\r\n"))
        #     # f.write(str(_item))

        # s = "\r\n"
        # with open("keys.txt","a+") as f:
        #     for i in _item:
        #         s = s + "-----" + str(i) +"\r\n"
        #
        #     f.write(s)

