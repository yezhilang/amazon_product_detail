import pymysql

import json

class mySQLHelper(object):
    def __init__(self, host='127.0.0.1', user='root', password='', charset='utf-8',db='amazon_product_detail'):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.db = db
        self.a = "abccdefsd"

        try:
            self.conn = pymysql.connect(host=self.host,
                                        user=self.user,
                                        password=self.password,
                                        db=self.db,
                                        charset='utf8mb4')
            self.cursor = self.conn.cursor()
        except:
            print("can't connect mysql")


    def query(self,sql):
        # try:
        self.cursor.execute(sql)
        self.conn.commit()
        rows = self.cursor.fetchall()
        return rows
        # except:
        #     print("can't query mysql")



    def insert(self,sql):
        try:
            rows = self.cursor.execute(sql)
        except:
            pass

    # def insertIntoProductInfo(self,data):
    #     sql = sql = "insert into product_info" \
    #           "(gs_user,gs_goods,gs_chips_price,gs_chips_num,gs_chips_total_price,gs_gussing_target,gs_gussing_direction,gs_gussing_start_time,gs_gussing_finish_time,gs_gussing_current_price,gs_goods_discount,gs_gussing_total_time)" \
    #           "VALUES" \
    #           "('{gs_user}','{gs_goods}','{gs_chips_price}','{gs_chips_num}','{gs_chips_total_price}','{gs_gussing_target}','{gs_gussing_direction}','{gs_gussing_start_time}','{gs_gussing_finish_time}','{gs_gussing_current_price}','{gs_goods_discount}','{gs_gussing_total_time}');" \
    #           "".format(
    #         gs_user=data["gs_user"],
    #         gs_goods = data["gs_goods"],
    #         gs_chips_price = data["gs_chips_price"],
    #         gs_chips_num = data["gs_chips_num"],
    #         gs_chips_total_price= data["gs_chips_total_price"],
    #         gs_gussing_target= data["gs_gussing_target"],
    #         gs_gussing_direction= data["gs_gussing_direction"],
    #         gs_gussing_start_time= data["gs_gussing_start_time"],
    #         gs_gussing_finish_time= data["gs_gussing_finish_time"],
    #         gs_gussing_current_price = data["gs_gussing_current_price"],
    #         gs_goods_discount = data["gs_goods_discount"],
    #         gs_gussing_total_time = data["gs_gussing_total_time"],
    #     )




if __name__ == "__main__":
    d = mySQLHelper()
    a = d.query("show tables;")
    print(a)

