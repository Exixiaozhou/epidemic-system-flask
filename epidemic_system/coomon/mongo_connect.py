import pymongo


class MONGO_CONNECT(object):
    def __init__(self):
        self.username = ''  # mongo数据库的信息
        self.password = ''
        self.host = ''
        self.port = 27017

        self.conn = pymongo.MongoClient(host=self.host, port=self.port, username=self.username, password=self.password)
        """ 创建数据库,以及文档 """
        self.db = self.conn['spider_result_save']
        self.cursor = self.db['epidemic_data']

    def insert_one_data(self, data):
        """ 插入一行数据集合 """
        self.cursor.insert_one(data)

    def update_one_data(self, modified, data):
        """ 修改一行数据集合 """
        self.cursor.update_one(modified, data)

    def insert_many_data(self, data):
        """ 插入多行数据集合 """
        self.cursor.insert_many(data)

    def data_find(self, keys):
        result = self.cursor.find({'insert_times': keys}, {"_id": 0})
        return result


def data_find(keys):
    mg_db = MONGO_CONNECT()
    result = mg_db.data_find(keys=keys)
    return result
