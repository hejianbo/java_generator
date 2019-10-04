import os
import shutil

import pymysql
import configparser

import config.basic_config as config
from myparser import TemplateParser


if __name__ == "__main__":
    # 获取当前所在目录
    current_dir = os.path.dirname(__file__)

    # 加载config.ini配置文件
    conf = configparser.ConfigParser()
    config_file_path = os.path.join(current_dir, "config.ini")
    conf.read(config_file_path, "utf-8")

    # 文件输出目录
    output_dir = os.path.join(current_dir, "output")
    # 清空输出文件夹
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    try:
        # 打开数据库连接
        db = pymysql.connect(host=conf.get("db", "db_host"),
                             database=conf.get("db", "db_name"),
                             user=conf.get("db", "db_user"),
                             password=conf.get("db", "db_password"))
        # 创建cursor
        cursor = db.cursor()

        templateParser = TemplateParser(current_dir, output_dir)
        # 循环处理每个数据库表
        for table in conf.get("db", "db_tables").split(","):
            # 使用execute执行sql
            cursor.execute("desc " + table)
            rows = cursor.fetchall()
            # 输出模板
            templateParser.render(table, rows, "dao/entity.jinja2", config.entity_package, 'entity_name', '.java')
            templateParser.render(table, rows, "dao/mapper.jinja2", config.mapper_package, 'mapper_name', '.java')
            templateParser.render(table, rows, "dao/dao.jinja2", config.dao_package, 'dao_name', '.java')
            templateParser.render(table, rows, "dao/dao.interface.jinja2", config.dao_interface_package, 'dao_interface_name', '.java')
            templateParser.render(table, rows, "dao/mapper/mapper.xml.jinja2", "resources", 'mapper_name', '.xml')
            templateParser.render(table, rows, "dao/service/service.bo.jinja2", config.service_bo_package, 'service_bo_name', '.java')

    finally:
        # 关闭数据库
        db.close()
