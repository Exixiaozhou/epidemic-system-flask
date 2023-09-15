from flask.views import MethodView
from flask import render_template
from flask import jsonify
from epidemic_system.db import service


class GET_TIMES(MethodView):
    """ 获取当前时间数据 """
    __methods__ = ['GET']

    def get(self):
        result = service.get_times()
        response = jsonify(result)
        return response


class GET_LABEL_NUMBER(MethodView):
    """ 获取每天最新的国内疫情统计数据, 前端标签数据：累计确诊,现有确诊,累计治愈,累计死亡 """
    __methods__ = ['GET']

    def get(self):
        result = service.get_label_number()
        response = jsonify(result)
        return response


class GET_LINE_DATA(MethodView):
    """ 获取最新的7天数据, 前端的折线图 """
    __methods__ = ['GET']

    def get(self):
        result = service.get_line_data()
        response = jsonify(result)
        return response


class GET_BAR_DATA(MethodView):
    """ 获取确诊率前10的城市, 前端柱状图 """
    __methods__ = ["GET"]

    def get(self):
        result = service.get_bar_data()
        response = jsonify(result)
        return response


class GET_PIE_DATA(MethodView):
    """ 获取国外疫情累计确诊率前10的数据, 前端饼图 """
    __methods__ = ["GET"]

    def get(self):
        result = service.get_pie_data()
        response = jsonify(result)
        return response


class GET_PROVINCE_DATA(MethodView):
    """ 随机获取每个省份的数据, 前端变动柱状图 """
    __methods__ = ["GET"]

    def get(self):
        result = service.get_province_data()
        response = jsonify(result)
        return response


class GET_MAP_DATA(MethodView):
    """ 获取全国的累计确诊率数据, 前端地图 """
    __methods__ = ["GET"]

    def get(self):
        result = service.get_map_data()
        response = jsonify(result)
        return response


class GET_EPIDEMIC_SYSTEM(MethodView):
    """ 返回渲染的html """

    __methods__ = ['GET']

    def get(self):
        return render_template('main_v1.html')
