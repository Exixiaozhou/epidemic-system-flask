import requests
import json
import re
import time
import random
from epidemic_system.coomon.mysql_connect import MYSQL_CONNECT
from epidemic_system.coomon.mongo_connect import MONGO_CONNECT
from epidemic_system.coomon import utils


class EPIDEMIC_SPIDER(object):
    """ 疫情实时动态采集 """
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41'
        }
        self.url = 'https://sa.sogou.com/new-weball/page/sgs/epidemic?type_page=pcpop'
        self.string_text = self.request_html()
        self.mysql_cursor = MYSQL_CONNECT()
        self.mongo_cursor = MONGO_CONNECT()

    def request_html(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.encoding = 'utf8'
        string_text = re.search(pattern='window.__INITIAL_STATE__ = (.*?)</script>', string=response.text, flags=re.S)
        return string_text.group(1)

    def domestic_stats_spider(self):
        """ 国内疫情标签总量数据 """
        table_name = 'domestic_stats'
        find_tables = f"select * from information_schema.TABLES where TABLE_NAME = '{table_name}'"
        if len(self.mysql_cursor.sql_find_execute(find_tables)) < 1:
            create_table_sql = f"create table {table_name}(diagnosed int,cured int,suspect int,death int," \
                               f"current_confirmed_count int,no_infect_count int,imported_count int," \
                               f"serious_count int,insert_times varchar(50));"
            self.mysql_cursor.create_table(create_table_sql)
        data_json = json.loads(self.string_text)['data']['domesticStats']
        """ 累计确诊,累计治愈,现有疑似,累计死亡,现有确诊,无症状感染者,境外输入,现有重症, """
        diagnosed = data_json['diagnosed']
        cured = data_json['cured']
        suspect = data_json['suspect']
        death = data_json['death']
        current_confirmed_count = data_json['currentConfirmedCount']
        no_infect_count = data_json['noInfectCount']
        imported_count = data_json['importedCount']
        serious_count = data_json['seriousCount']
        insert_times = time.strftime('%Y-%m-%d')
        find_sql = f"select * from {table_name} where insert_times = '{insert_times}'"
        insert_sql = f"INSERT INTO {table_name}(diagnosed,cured,suspect,death,current_confirmed_count," \
                     f"no_infect_count,imported_count,serious_count,insert_times) values({diagnosed},{cured}," \
                     f"{suspect},{death},{current_confirmed_count},{no_infect_count},{imported_count}," \
                     f"{serious_count},'{insert_times}')"
        update_sql = f"UPDATE {table_name} set diagnosed={diagnosed},cured={cured},suspect={suspect},death={death}," \
                     f"current_confirmed_count={current_confirmed_count},no_infect_count={no_infect_count}," \
                     f"imported_count={imported_count},serious_count={serious_count} where insert_times='" \
                     f"{insert_times}'"
        if len(self.mysql_cursor.sql_find_execute(find_sql)) > 0:
            self.mysql_cursor.sql_execute(update_sql)
        else:
            self.mysql_cursor.sql_execute(insert_sql)

    def domestic_area_spider(self):
        """ 全国各地区域数据采集 """
        table_name = 'domestic_area'
        find_tables = f"select * from information_schema.TABLES where TABLE_NAME = '{table_name}'"
        if len(self.mysql_cursor.sql_find_execute(find_tables)) < 1:
            create_table_sql = f"create table {table_name}(province_name varchar(50) character set utf8," \
                               f"current_confirmed_count int,confirmed_count int,cured_count int,dead_count int," \
                               f"insert_times varchar(50));"
            self.mysql_cursor.create_table(create_table_sql)
        data_json = json.loads(self.string_text)['data']['area']
        self.data_extract(data_json=data_json, table_name=table_name)

    def foreign_area_spider(self):
        """ 国外疫情数据采集 """
        table_name = 'foreign_area'
        find_tables = f"select * from information_schema.TABLES where TABLE_NAME = '{table_name}'"
        if len(self.mysql_cursor.sql_find_execute(find_tables)) < 1:
            create_table_sql = f"create table {table_name}(province_name varchar(50) character set utf8," \
                               f"current_confirmed_count int,confirmed_count int,cured_count int,dead_count int," \
                               f"insert_times varchar(50));"
            self.mysql_cursor.create_table(create_table_sql)
        data_json = json.loads(self.string_text)['data']['overseas']
        self.data_extract(data_json=data_json, table_name=table_name)

    def data_extract(self, data_json, table_name):
        """ 地区,现有确诊,累计确诊,治愈,死亡 """
        for items in data_json:
            province_name = items['provinceName']
            current_confirmed_count = items['currentConfirmedCount']
            confirmed_count = items['confirmedCount']
            cured_count = items['curedCount']
            dead_count = items['deadCount']
            insert_times = time.strftime('%Y-%m-%d')
            find_sql = f"select * from {table_name} where province_name='{province_name}' and insert_times='" \
                       f"{insert_times}';"
            insert_sql = f"INSERT INTO {table_name} (province_name,current_confirmed_count,confirmed_count," \
                         f"cured_count,dead_count,insert_times) values('{province_name}',{current_confirmed_count}," \
                         f"{confirmed_count},{cured_count},{dead_count},'{insert_times}');"
            update_sql = f"UPDATE {table_name} set province_name='{province_name}',current_confirmed_count=" \
                         f"{current_confirmed_count},confirmed_count={confirmed_count},cured_count={cured_count}," \
                         f"cured_count={cured_count},dead_count={dead_count} where province_name='{province_name}' " \
                         f"and insert_times='{insert_times}';"
            if len(self.mysql_cursor.sql_find_execute(find_sql)) > 0:
                self.mysql_cursor.sql_execute(update_sql)
            else:
                self.mysql_cursor.sql_execute(insert_sql)

    def epidemic_data_insert_mongo(self, insert_times=None):
        """ 向mongo数据库插入所有的疫情数 """
        data_json = json.loads(self.string_text)
        items = {
            'insert_times': insert_times, 'data_json': data_json
        }
        self.mongo_cursor.insert_one_data(items)
        return True

    def epidemic_data_update_mongo(self):
        insert_times = time.strftime('%Y-%m-%d')
        result = self.mongo_cursor.data_find(insert_times)
        if len(list(result)) < 1:
            """ mongo不存在当天的数据则调用爬虫采集功能 """
            self.epidemic_data_insert_mongo(insert_times)
        data_json = json.loads(self.string_text)
        modified = {
            'insert_times': insert_times
        }
        items = {
             '$set': {'insert_times': insert_times, 'data_json': data_json}
        }
        self.mongo_cursor.update_one_data(modified, items)

    def province_data_extract(self):
        """ 在mongo数据库不存在的情况，调用爬虫实时采集数据 """
        data_json = json.loads(self.string_text)['data']['area']
        i = random.randint(0, len(data_json)-1)
        province_name = data_json[i]['provinceName']
        province_name_list = list()
        confirmed_count_list = list()
        if len(data_json[i]['cities']) < 1:
            province_name_list.append(data_json[i]['provinceName'])
            confirmed_count_list.append(data_json[i]['confirmedCount'])
        else:
            for data in data_json[i]['cities']:
                province_name_list.append(data['city'])
                confirmed_count_list.append(data['confirmedCount'])
        items = {
            'province_name': province_name, 'province_name_list': province_name_list,
            'confirmed_count_list': confirmed_count_list
        }
        color_list = utils.random_color(number=len(items) - 2)
        items['color_list'] = color_list
        return items


# runs = EPIDEMIC_SPIDER()
# runs.domestic_stats_spider()
# runs.domestic_area_spider()
# runs.foreign_area_spider()
# runs.province_data_extract()
# runs.epidemic_data_save_mongo()
