# encoding:utf-8
from mySQLHelper import mySQLHelper

class taskModel(object):

    def __init__(self):
        self.db = mySQLHelper(db="products")
        self.initializeDb()

    def initializeDb(self):
        sql = "desc sdb_index_product_2617941011"
        res = self.db.query(sql)
        flag = False

        for i in res:
            print i
            if i[0] == "crawled":
                flag = True
        if not flag:
            sql = "alter table sdb_index_product_2617941011 add column crawled varchar(5) not null default 'n'"
            self.db.query(sql)
    def getTasks(self):
        sql = "select asin from sdb_index_product_2617941011 where crawled='n' limit 0,500"
        res = self.db.query(sql)
        l = []
        for i in res:
            print i
            l.append(i[0].encode("utf-8"))
        return l

    def finishTask(self,asin):
        sql = "update sdb_index_product_2617941011 set crawled='y' where asin='"+asin+"';"
        self.db.query(sql)


if __name__ == "__main__":
    tm = taskModel()
    tm.initializeDb()
    print tm.getTasks()
    tm.finishTask("031235925X")