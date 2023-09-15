import time
import random
from epidemic_system.coomon import mysql_connect
from epidemic_system.coomon import mongo_connect
from epidemic_system.coomon import utils
from epidemic_system.spiders import service


def get_times():
    times_text = time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')
    return str(times_text)


def get_label_number():
    """ 从数据库中查询国内疫情统计数据 """
    sql = 'select * from domestic_stats order by insert_times desc limit 1'
    result = mysql_connect.sql_execute(sql)
    return result[0]


def get_line_data():
    """ 提取七天的国内疫情统计数据 """
    times_list = list()
    diagnosed_list = list()
    cured_list = list()
    current_confirmed_count_list = list()
    death_list = list()
    sql = 'select * from domestic_stats order by insert_times desc limit 7'
    result = mysql_connect.sql_execute(sql)
    result.reverse()
    for data in result:
        times_list.append(data.get('insert_times'))
        diagnosed_list.append(data.get('diagnosed'))
        cured_list.append(data.get('cured'))
        current_confirmed_count_list.append(data.get('current_confirmed_count'))
        death_list.append(data.get('death'))
    items = {
        'times_list': times_list, 'diagnosed_list': diagnosed_list, 'cured_list': cured_list,
        'current_confirmed_count_list': current_confirmed_count_list, 'death_list': death_list
    }
    color_list = utils.random_color(number=len(items)-1)
    items['color_list'] = color_list
    return items


def get_bar_data():
    """ 提取前10的全国各地区分布数据 """
    province_name_list = list()
    current_confirmed_count_list = list()
    dead_count_list = list()
    insert_times = time.strftime('%Y-%m-%d')
    sql = f"select * from domestic_area where insert_times='{insert_times}' order by current_confirmed_count desc"
    result = mysql_connect.sql_execute(sql)
    for data in result[:10]:
        province_name_list.append(data.get('province_name', None))
        current_confirmed_count_list.append(data.get('current_confirmed_count', 0))
        dead_count_list.append(data.get('dead_count', 0))
    items = {
        'province_name_list': province_name_list, 'current_confirmed_count_list': current_confirmed_count_list,
        'dead_count_list': dead_count_list
    }
    color_list = utils.random_color(number=len(items)-1)
    items['color_list'] = color_list
    return items


def get_pie_data():
    """ 国外疫情数据获取 """
    data_list = list()
    insert_times = time.strftime('%Y-%m-%d')
    sql = f"select * from foreign_area where insert_times='{insert_times}' order by current_confirmed_count " \
          f"desc limit 10"
    result = mysql_connect.sql_execute(sql)
    for data in result:
        data_list.append({"name": data.get('province_name'), 'value': data.get('current_confirmed_count')})
    color_list = utils.random_color(number=len(result))
    items = {
        'data_list': data_list, 'color_list': color_list
    }
    return items


def get_province_data():
    """ 省份数据提取 """
    insert_times = time.strftime('%Y-%m-%d')
    result = mongo_connect.data_find(insert_times)
    if len(list(result)) < 1:
        spider_obj = service.EPIDEMIC_SPIDER()
        """ mongo不存在当天的数据则调用爬虫采集功能 """
        spider_obj.epidemic_data_insert_mongo(insert_times=insert_times)
    result = mongo_epidemic_get(keys=insert_times)
    return result


def mongo_epidemic_get(keys):
    """ 从mongo数据库中查询当前的数据 """
    result = mongo_connect.data_find(keys=keys)
    for item in result:
        data_json = item['data_json']['data']['area']
        i = random.randint(0, len(data_json) - 1)
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


def get_map_data():
    """ 地图全国数据 """
    data_list = list()
    insert_times = time.strftime('%Y-%m-%d')
    sql = f"select * from domestic_area where insert_times='{insert_times}'"
    result = mysql_connect.sql_execute(sql)
    for data in result:
        data_list.append({"name": data.get('province_name'), "value": data.get('confirmed_count')})
    return data_list
