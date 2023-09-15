from datetime import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from epidemic_system.spiders.service import EPIDEMIC_SPIDER
from epidemic_system.coomon import utils
from epidemic_system.conf.loggers import logger


def spider_timing_task():
    """ 数据采集定时任务 """
    spider_obj = EPIDEMIC_SPIDER()
    """ 国内疫情标签总量数据采集 """
    spider_obj.domestic_stats_spider()
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 执行了:全国各地区域数据采集")
    """ 全国各地区域数据采集 """
    spider_obj.domestic_area_spider()
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 执行了:国内疫情标签总量数据采集")
    """ 国外疫情数据采集 """
    spider_obj.foreign_area_spider()
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 执行了:国外疫情数据采集")
    """ mongo不存在当天的数据,则调用向mongo数据库插入所有的疫情数,否则修改 """
    spider_obj.epidemic_data_update_mongo()
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 执行了:mongo不存在当天的数据,mongo数据库插入所有的疫情数,否则修改")


def start_timing_task():
    """ 创建定时任务, 并设置时区 """
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    """ 在特定时间周期性地触发, func=执行的方法, trigger=触发类型, args=参数 """
    # scheduler.add_job(func=spider_timing_task, trigger='cron', hour='16', minute='2')  # minute='35'
    scheduler.add_job(func=spider_timing_task, trigger='interval', minutes=1)
    """ 启动 """
    scheduler.start()


logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 触发了定时任务")
start_timing_task()
