from .mySQLHelper import mySQLHelper

class iniDB(object):


    def __init__(self):
        self.db = mySQLHelper()

    def createTableIfNotExists(self):
        sql = "create table if not exists product_info (id int auto_increment primary key,asin varchar(10) not null unique,sprddetail1 text,sprddetail2 text,frequently_bought text,customers_also_bought text,customers_also_view text,campare_similar_products text,stars_reviews text,best_seller_rank text,price varchar(10),category varchar(100),time datetime not null);"
        self.db.query(sql)
