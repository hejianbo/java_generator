import os
import shutil

import pymysql

from config.config_util import ConfigUtil
from config.dal_config import DalConfig
from config.db_config import DbConfig
from config.service_config import ServiceConfig
from myparser import TemplateParser
from myparser.template_item import TemplateItem
from util.template_item_factory import TemplateItemFactory

if __name__ == "__main__":
    # 获取当前所在目录
    current_dir = os.path.dirname(__file__)

    # 加载config.ini配置文件
    conf = ConfigUtil.get_config(current_dir, "config.ini")

    # 加载配置文件到对象中
    db_config = DbConfig(conf)
    dal_config = DalConfig(conf)
    service_config = ServiceConfig(conf)

    # 文件输出目录
    output_dir = os.path.join(current_dir, "output")
    # 清空输出文件夹
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    try:
        # 打开数据库连接
        db = pymysql.connect(host=db_config.db_host,
                             database=db_config.db_name,
                             user=db_config.db_user,
                             password=db_config.db_password)
        # 创建cursor
        cursor = db.cursor()

        templateParser = TemplateParser(current_dir, output_dir, conf)

        templateItemFactory = TemplateItemFactory(conf, os.path.join(current_dir, "template.ini"))

        # 循环处理每个数据库表
        for table in db_config.db_tables.split(","):
            # 使用execute执行sql
            cursor.execute("desc " + table)
            rows = cursor.fetchall()

            for templateItem in templateItemFactory.get_template_items():
                templateParser.render2(
                    TemplateItem(table, rows, templateItem["template_path"], templateItem["output_dir"], templateItem["template_name"], templateItem["file_type"]))

            # # 输出模板
            # templateParser.render2(
            #     TemplateItem(table, rows, "dao/entity.jinja2", dal_config.entity_package, 'entity_name', '.java'))
            # templateParser.render2(
            #     TemplateItem(table, rows, "dao/mapper.jinja2", dal_config.mapper_package, 'mapper_name', '.java'))
            # templateParser.render2(
            #     TemplateItem(table, rows, "dao/dao.jinja2", dal_config.dao_package, 'dao_name', '.java'))
            # templateParser.render2(
            #     TemplateItem(table, rows, "dao/dao.interface.jinja2", dal_config.dao_interface_package,
            #                  'dao_interface_name', '.java'))
            # templateParser.render2(
            #     TemplateItem(table, rows, "dao/mapper/mapper.xml.jinja2", "resources", 'mapper_name', '.xml'))
            # templateParser.render2(
            #     TemplateItem(table, rows, "dao/service/service.bo.jinja2", service_config.service_bo_package,
            #                  'service_bo_name', '.java'))
    finally:
        # 关闭数据库
        cursor.close()
        db.close()
