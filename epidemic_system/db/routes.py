from flask import Blueprint
from epidemic_system.db.controller import GET_TIMES
from epidemic_system.db.controller import GET_LABEL_NUMBER
from epidemic_system.db.controller import GET_LINE_DATA
from epidemic_system.db.controller import GET_BAR_DATA
from epidemic_system.db.controller import GET_PIE_DATA
from epidemic_system.db.controller import GET_PROVINCE_DATA
from epidemic_system.db.controller import GET_MAP_DATA
from epidemic_system.db.controller import GET_EPIDEMIC_SYSTEM


GET_DATA = Blueprint('get_data', __name__, static_folder='', static_url_path='')

# 蓝图注册类视图
GET_DATA.add_url_rule('/get_times', view_func=GET_TIMES.as_view('GET_TIMES'))
GET_DATA.add_url_rule('/get_label_data', view_func=GET_LABEL_NUMBER.as_view('GET_LABEL_NUMBER'))
GET_DATA.add_url_rule('/get_line_data', view_func=GET_LINE_DATA.as_view('GET_LINE_DATA'))
GET_DATA.add_url_rule('/get_bar_data', view_func=GET_BAR_DATA.as_view('GET_BAR_DATA'))
GET_DATA.add_url_rule('/get_pie_data', view_func=GET_PIE_DATA.as_view('GET_PIE_DATA'))
GET_DATA.add_url_rule('/get_province_data', view_func=GET_PROVINCE_DATA.as_view('GET_PROVINCE_DATA'))
GET_DATA.add_url_rule('/get_map_data', view_func=GET_MAP_DATA.as_view('GET_MAP_DATA'))
GET_DATA.add_url_rule('/get_epidemic_system', view_func=GET_EPIDEMIC_SYSTEM.as_view('GET_EPIDEMIC_SYSTEM'))
