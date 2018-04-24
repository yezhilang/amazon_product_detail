# encoding:utf-8
import re
import sys
import time

import requests
from lxml import etree

# import datetime
from amazon_product_detail.spiders.Dbmodels.productInfoModel import productInfo

reload(sys)
sys.setdefaultencoding('utf-8')
class parser(object):

    def __init__(self, html,asin):

        self.html = html
        self.asin = asin
        self.s = requests.session()
        self.headers = {
            "User-Agent":"Mozila/5.0"
        }

    def extractData(self):

        print "sprddetail1 start:"+time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            sprddetail1 = "||".join(self.s_p_r_detail1_parse())
        except:
            sprddetail1 = None
        print "sprddetail1 finished:" + time.strftime("%Y-%m-%d %H:%M:%S")

        print "sprddetail2 start:" + time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            sprddetail2 = "||".join(self.s_p_d_detail2_parse())
        except:
            sprddetail2 = None
        print "sprddetail2 start:" + time.strftime("%Y-%m-%d %H:%M:%S")

        print "frequentlyBought start:" + time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            frequentlyBought = "||".join(self.getFrequentlyBought())
        except:
            frequentlyBought = None
        print "frequentlyBought finished:" + time.strftime("%Y-%m-%d %H:%M:%S")

        print "customsAlsoView start:" + time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            customsAlsoView = "||".join(self.c_w_v_parse())
        except:
            customsAlsoView = None
        print "customsAlsoView finished:" + time.strftime("%Y-%m-%d %H:%M:%S")

        try:
            customAlsoBought = "||".join(self.c_w_b_parse())
        except:
            customAlsoBought = None
        try:
            compareSimilarProduts =str(self.c_w_similar_items_parse()).replace("\"","\\\"")
        except:
            compareSimilarProduts = None

        try:
            stars_reviews = str(self.parse_stars()).replace("\"","\\\"")
        except:
            stars_reviews = None

        try:
             bestSellerRank = str(self.parse_best_seller_rank()).replace("\"","\\\"")
        except:
            bestSellerRank = None

        try:
            price = str(self.parse_price()).replace("\"","\\\"")
        except:
            price = None

        try:
            category = str(self.parse_category()).replace("\"","\\\"")
        except:
            category = None

        # sprddetail1 = "||".join(self.s_p_r_detail1_parse())
        #
        # sprddetail2 = "||".join(self.s_p_d_detail2_parse())
        #
        # frequentlyBought = "||".join(self.getFrequentlyBought())
        #
        # customsAlsoView = "||".join(self.c_w_v_parse())
        #
        # customAlsoBought = "||".join(self.c_w_b_parse())
        #
        # compareSimilarProduts =str(self.c_w_similar_items_parse())

        return {
            "sprddetail1":sprddetail1,
            "sprddetail2":sprddetail2,
            "frequentlyBought":frequentlyBought,
            "customsAlsoView":customsAlsoView,
            "customsAlsoBought":customAlsoBought,
            "compareSimilarProducts":compareSimilarProduts,
            "stars&reviews":stars_reviews,
            "bestSellerRank":bestSellerRank,
            "price":price,
            "category":category,
            "asin":self.asin
        }

    def s_p_r_detail1_parse(self):

        selector = etree.HTML(self.html)
        x = eval(selector.xpath("//div[@id='sp_detail']/@data-a-carousel-options")[0].replace("false", "False"))
        # y = eval(selector.xpath("//div[@id='sp_detail2']/@data-a-carousel-options")[0].replace("false", "False"))
        request_data_size = 500
        params = x["ajax"]["params"]
        params["num"] = request_data_size
        params["count"] = request_data_size
        params["oData"] = x["initialSeenAsins"]
        params["offset"] = params["start"]
        params["tot"] = x["set_size"]
        params["pg"] = 1 if int(params["cc"]) == 0 else 2
        params["_"] = str(long(time.time() * 1000))

        l = [i for i in x["initialSeenAsins"]]
        flag = True
        while (flag):
            LEN = len(l)
            url_para = ""
            for i in params:
                url_para = url_para + "&" + str(i) + "=" + str(params[i])
            url_para = url_para[1::]
            base_url = "https://www.amazon.com/gp/nemo/spd/handlers/spd-shov.html?"
            url = base_url + url_para
            r = self.s.get(url=url, headers=self.headers)
            response_data = eval(r.text.strip())

            for i in response_data["data"]:
                if i["oid"].strip() not in l:
                    l.append(i["oid"].strip())
                    # print("new data ", i["oid"])
            if LEN == len(l):
                # print("crawl is finished...")
                break
            params["pg"] = params["pg"] + 1
            LEN = len(l)
            params["cc"] = params["start"] = str((int(LEN) / 5) * 5)

            params["oData"] = str(l).replace("\'", "\"")
            params["_"] = str(long(time.time() * 1000))

            return list(set(l))



# def getField(field, html):
#     print("into")
#     if field not in html:
#         return None
#
#     repattern = "<\w+|\"" \
#                 ">?"+field
#
#     print(repattern)
#
#     target_item = re.findall(repattern, html)
#
#     print(target_item)
#
# url = 'https://www.amazon.com/dp/B01CTYUFGS'
# headers = {
#     "User-Agent":"Mozila/5.0"
# }
#
# s = requests.session()
# r = s.get(url=url, headers=headers)
# # print(r.text)
# getField("Shipping Weight",r.text)

    def s_p_d_detail2_parse(self):
        selector = etree.HTML(self.html)

        # x = eval(selector.xpath("//div[@id='sp_detail']/@data-a-carousel-options")[0].replace("false","False"))
        x = eval(selector.xpath("//div[@id='sp_detail2']/@data-a-carousel-options")[0].replace("false", "False"))

        request_data_size = 500
        params = x["ajax"]["params"]
        params["num"] = request_data_size
        params["count"] = request_data_size
        params["oData"] = x["initialSeenAsins"]
        params["offset"] = params["start"]
        params["tot"] = x["set_size"]
        params["pg"] = 1 if int(params["cc"]) == 0 else 2
        params["_"] = str(long(time.time() * 1000))

        l = [i for i in x["initialSeenAsins"]]
        flag = True
        while (flag):
            LEN = len(l)
            url_para = ""
            for i in params:
                url_para = url_para + "&" + str(i) + "=" + str(params[i])
            url_para = url_para[1::]
            base_url = "https://www.amazon.com/gp/nemo/spd/handlers/spd-shov.html?"
            url = base_url + url_para
            r = self.s.get(url=url, headers=self.headers)
            try:
                response_data = eval(r.text.strip())
            except:
                # print("crawler is finished...")
                break

            for i in response_data["data"]:
                if i["oid"].strip() not in l:
                    l.append(i["oid"].strip())
                    # print("new data ", i["oid"])
            if LEN == len(l):
                print("crawl is finished...")
                break
            params["pg"] = params["pg"] + 1
            LEN = len(l)
            params["cc"] = params["start"] = str((int(LEN) / 5) * 5)
            # double quote replace single quote, which is very important,
            # or the server can't regnize the yet-viewd item and the response from the very beginning of the set
            params["oData"] = str(l).replace("\'", "\"")
            params["_"] = str(long(time.time() * 1000))
            # print("now the length of crawed-list is ", len(l))

        return list(set(l))

    def getFrequentlyBought(self):

        related_products = []
        selector = etree.HTML(self.html)
        li = selector.xpath("//*[@id='sims-fbt-form']/div[1]/ul/li")

        for i in li:
            try:
                href = i.xpath("./span/a/@href")[0]
            except:
                continue
            # print(href)
            related_products.append(re.findall("dp/.*?/", href)[0][3:-1])

        return related_products if related_products else None

    def c_w_v_parse(self):

        selector = etree.HTML(self.html)
        data = selector.xpath("//div[@id='session-sims-feature']/div[1]/@data-a-carousel-options")[0]
        # print(data)

        data = eval(data)
        params = data["ajax"]["params"]
        # print(data["ajax"]["id_list"])
        # print(type(data["ajax"]["id_list"]))
        params["asins"] = ",".join(data["ajax"]["id_list"])
        params["count"] = 500
        params["offset"] = data["set_size"]
        params["_"] = str(long(time.time() * 1000))
        url_para = ""
        target_data = [i for i in data["ajax"]["id_list"]]
        for i in params:
            url_para = url_para + "&" + str(i) + "=" + str(params[i])
        url_para = url_para[1::]
        base_url = "https://www.amazon.com/gp/p13n-shared/faceout-partial?"
        url = base_url + url_para
        r = self.s.get(url=url, headers=self.headers)

        # print(r.text)

        response_data = eval(r.text)
        # print(response_data)
        # print(target_data, "before parse the length is ", len(target_data))
        for i in response_data["data"]:
            # print(i)
            selector = etree.HTML(i)
            asin = selector.xpath("//div[@class='a-section a-spacing-none p13n-asin']/@data-p13n-asin-metadata")[0]
            target_data.append(eval(asin)["asin"])
            # print(eval(asin)["asin"])

        return list(set(target_data))

    def c_w_b_parse(self):
        selector = etree.HTML(self.html)
        data = selector.xpath("//div[@id='purchase-sims-feature']/div[1]/@data-a-carousel-options")[0]
        data = eval(data)
        params = data["ajax"]["params"]
        params["asins"] = ",".join(data["ajax"]["id_list"])
        params["count"] = 500
        params["offset"] = data["set_size"]
        params["_"] = str(long(time.time() * 1000))
        url_para = ""
        target_data = [i for i in data["ajax"]["id_list"]]
        for i in params:
            url_para = url_para + "&" + str(i) + "=" + str(params[i])
        url_para = url_para[1::]
        base_url = "https://www.amazon.com/gp/p13n-shared/faceout-partial?"
        url = base_url + url_para
        r = self.s.get(url=url, headers=self.headers, verify=False)
        response_data = eval(r.text)
        print(target_data, "before parse the length is ", len(target_data))
        for i in response_data["data"]:
            selector = etree.HTML(i)
            asin = selector.xpath("//div[@class='a-section a-spacing-none p13n-asin']/@data-p13n-asin-metadata")[0]
            target_data.append(eval(asin)["asin"])
        return list(set(target_data))

    def c_w_similar_items_parse(self):
        selector = etree.HTML(self.html)

        trs = selector.xpath("//*[@id='HLCXComparisonTable']/tr")
        this_asin = "thisasin"
        counter = 1
        campare = {}
        for tr in trs:
            l = []
            if counter == 1:
                xpath = "./th"
                subitems = tr.xpath(xpath)
                _key = "category"
                asins = []
                _as = ""
                for items in subitems:
                    asxpath = "./a[1]/@href"
                    try:
                        _as = re.findall("/dp/.*?/", items.xpath(asxpath)[0].strip())[0][4:-1]
                    except:
                        _as = this_asin
                    asins.append(_as)
                    v = ""
                    xpath = ".//*"
                    item = items.xpath(xpath)
                    for text in item:
                        try:
                            v = v + text.xpath("./text()")[0].strip()
                        except:
                            continue
                    l.append(v)
                campare["asin"] = str(asins)
                campare[_key] = str(l)
                counter = counter + 1
                continue
            if counter == 2 or counter == 3:
                counter = counter + 1
                continue
            _key = tr.xpath("./th[1]/span[1]/text()")[0].strip()
            xpath = "./td"
            subitems = tr.xpath(xpath)
            for items in subitems:
                v = ""
                xpath = ".//*"
                item = items.xpath(xpath)
                for text in item:
                    try:
                        v = v + text.xpath("./text()")[0].strip()
                    except:
                        continue
                if v:
                    l.append(v)

                _value = str(l)
                campare[_key] = _value
                counter = counter + 1
        l = []
        counter = 0
        for i in campare["category"]:
            d = {}
            for j in campare.keys():
                d[j] = eval(campare[j])[counter]
            counter = counter + 1
            l.append(d)
            if counter == len(eval(campare["category"])):
                break
        for i in l:
            i["Price"] = i["Price"].split("$")[1]
            # print i
        return l

    def parse_best_seller_rank(self):
        selector = etree.HTML(self.html)
        data = []
        try:
            li = selector.xpath("//*[@id='SalesRank']")[0]


            text = li.xpath("./text()")[1].strip()[:-1]

            subli = li.xpath(".//li")

            for i in subli:
                t = i.xpath(".//*")
                for j in t:
                    try:
                        text = text + (j.xpath("./text()")[0].strip()) + "->"
                        print "-----"+text
                    except:
                        continue
            text = text[1::]
            l = text.split("#")
            data = []
            for i in l:
                item = i.split("in")
                data.append({
                    "Rank": item[0].strip() if ("->" not in item[0]) else item[0][:-2],
                    "Route":item[1].strip() if (item[1].strip()[0:2:] != "->") else item[1].strip()[2::],
                })
        except:
            try:

                trs = selector.xpath(".//*[@id='productDetails_detailBullets_sections1']/tr")
                for tr in trs:
                    text = tr.xpath("./th[1]/text()")[0].strip()
                    t = ""

                    print text
                    if "Rank" in text:
                        for subitem in tr.xpath(".//*"):
                            for i in subitem:

                                try:
                                    t = t + i.xpath("./text()")[0].strip()+"->"
                                except:
                                    continue
                                print i.xpath("./text()")[0].strip()

                        print t
                        t = t[3::].replace("in->See Top 100","")
                        print t
                        l = t.split("#")
                        print l
                        data = []
                        for i in l:

                            item = i.split("in")
                            # print item[1].strip()[0:2:] != "->"
                            data.append({
                                "Rank": item[0].strip() if ("->" not in item[0]) else item[0][:-2],
                                "Route": item[1].strip() if (item[1].strip()[-2:] != "->") else item[1].strip()[:-2:] if (item[1].strip()[:-2:][-1::] !="(") else item[1].strip()[:-3:].strip(),
                            })
                        break
            except:
                data = None

        return data if data else None

    def parse_stars(self):
        selector = etree.HTML(self.html)
        span = selector.xpath("//*[@id='detail-bullets']//span")

        productScore = ""
        for s in span:
            try:
                productScore = s.xpath("./text()")[0]
            except IndexError:
                 continue
            if "out of" in productScore:
                productScore = productScore.strip()
                break

        # productScore = selector.xpath("//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[5]/span/span[1]/a[2]/i/span/text()")[0].strip()
        a = selector.xpath("//*[@id='detail-bullets']//a")

        reviewNum = ""
        for i in a:
            try:
                reviewNum = i.xpath("./text()")[0].strip()
            except IndexError:
                continue
            # print(reviewNum)
            if "customer reviews" in reviewNum:
                break

        # reviewNum = selector.xpath("//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[5]/span/span[3]/a/text()")[0].strip()

        review_info = productScore + "||" + reviewNum
        if "out of" not in review_info:
            xpath = ".//*[@id='acrPopover']/@title"
            try:
                review_info = selector.xpath(xpath)[0].strip()
            except:
                return None
            if "out of" not in review_info:
                return None
        return review_info

    def parse_price(self):
        selector = etree.HTML(self.html)
        price = selector.xpath(".//*[@id='priceblock_ourprice']/text()")[0].strip()
        return price

    def parse_category(self):
        selector = etree.HTML(self.html)
        category = selector.xpath(".//*[@id='productTitle']/text()")[0].strip()
        return category

if __name__ == "__main__":
    s = requests.session()
    # url = "https://www.amazon.com/dp/B06WRMZZ45?ref=vs_aa_hp_t2r1c1_sennheiser_172541_desktop_vsf&pf_rd_r=J66STBBR31BV2WTDQW5Y&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=Landing&pf_rd_i=172541&pf_rd_p=27242288-ceef-48b8-ab11-db4a4820bbcc&pf_rd_s=merchandised-search-grid-t2-r2-c1"

    url = "https://www.amazon.com/dp/030758674X"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400"
    }
    print time.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        r = s.get(url=url,headers=headers)
        if r.status_code == 200:

            break
        print "status_code wrong , continue request "
    # print(r.status_code)
    p = parser(r.text,"030758674X")
    data = p.extractData()
    # print "-----------------------------------------------"
    for i in data:
        print {i:data[i]}
    #
    # data["asin"] = "B00N2BW638"
    # print "data="+str(data)
    # print data.keys()

    print time.strftime("%Y-%m-%d %H:%M:%S")

    p = productInfo()

    # p.insertIntoProductInfo(data)

