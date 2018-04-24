# coding:utf-8
# from newAmazonProductDetail.backupcode.product_parser import productParser
#
# parser = productParser()
#
# XPATH_RULE = {
#     "Item Weight":{
#         "parse_once":True,
#         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[1]/text()"
#     },
#     "Shipping Weight":{
#         "parse_once":True,
#         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[2]/text()[1]"
#     },
#     "ASIN":{
#         "parse_once":True,
#         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[3]/text()[1]"
#     },
#     "UPC":{
#         "parse_once":True,
#         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[4]/text()[1]"
#     },
#     "Average Customer Review":{
#         "parse_once":False,
#         "parse_rule":"",
#         "_value":parser.parse_stars
#     },
#    "Amazon Best Sellers Rank":{
#        "parse_once":False,
#        "parse_rule":"",
#        "_value":parser.parse_best_seller_rank
#    }
# }
#
# # XPATH_RULE = {
# #     "Item Weight":{
# #         "parse_once":True,
# #         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[1]/text()"
# #     },
# #     "Shipping Weight":{
# #         "parse_once":True,
# #         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[2]/text()[1]"
# #     },
# #     "ASIN":{
# #         "parse_once":True,
# #         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[3]/text()[1]"
# #     },
# #     "UPC":{
# #         "parse_once":True,
# #         "parse_rule":"//*[@id='detail-bullets']/table/tr/td/div[2]/ul/li[4]/text()[1]"
# #     },
# #     "Average Customer Review":{
# #         "parse_once":False,
# #         "parse_rule":"",
# #         "_value":""
# #     },
#    "Amazon Best Sellers Rank":{
#        "parse_once":False,
#        "parse_rule":"",
#        "_value":""
#    }
# }