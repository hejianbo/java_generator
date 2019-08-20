import os
import shutil

import pymysql

import config.basic_config as config
import config.db_config as dbconfig
from myparser import TemplateParser


if __name__ == "__main__":
    # 获取当前所在目录
    current_dir = os.path.dirname(__file__)
    # 文件输出目录
    output_dir = os.path.join(current_dir, "output")
    # 清空输出文件夹
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    try:
        # 打开数据库连接
        db = pymysql.connect(host=dbconfig.db_host, database=dbconfig.database, user=dbconfig.db_user, password=dbconfig.db_password)
        # 创建cursor
        cursor = db.cursor()

        templateParser = TemplateParser(current_dir, output_dir)
        # 循环处理每个数据库表
        for table in dbconfig.tables.split(","):
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
