import pymysql
import os
import shutil

from jinja2 import Environment, FileSystemLoader

import config.db_config as dbconfig
import config.basic_config as config
from myparser import EntityParser, TableNameParser


def generate_mapper_xml(table_columns):
    """
    生成mapper.xml
    :param table_columns: 表结构列数详细信息
    :return:
    """
    """
        生成dao接口
        :param table_columns: 表结构列数详细信息
        :return:
        """
    entity_parser = EntityParser(table_columns)
    # 转换为java中的字段
    columns = entity_parser.parse()
    # 获取类名
    table_name_parser = TableNameParser(table)
    names = table_name_parser.get_all_names()
    primary_keys = ', '.join(
        [column['property_type'] + ' ' + column['property'] for column in columns if column['is_primary'] is True])

    # 获取模板文件
    template = env.get_template("dao/mapper/mapper.xml.jinja2")
    response = template.render(columns=columns, names=names, primary_keys=primary_keys)

    mapper_output_dir = os.path.join(output_dir, "resources", "mappers")
    if not os.path.exists(mapper_output_dir):
        os.makedirs(mapper_output_dir)

    with open(os.path.join(mapper_output_dir, names['mapper_name'] + '.xml'), r'w') as f:
        f.write(response)


def generate_mapper(table_columns):
    """
    生成mapper类
    :param table_columns: 表结构列数详细信息
    :return:
    """
    entity_parser = EntityParser(table_columns)
    # 转换为java中的字段
    columns = entity_parser.parse()
    # 获取类名
    table_name_parser = TableNameParser(table)
    names = table_name_parser.get_all_names()
    primary_keys = ', '.join(
    ['@Param("' + column['property'] + '")' + column['property_type'] + ' ' + column['property'] for column in columns if column['is_primary'] is True])

    # 获取模板文件
    template = env.get_template("dao/mapper.jinja2")
    response = template.render(columns=columns, names=names, primary_keys=primary_keys)

    mapper_output_dir = os.path.join(output_dir, *config.mapper_package.split('.'))
    if not os.path.exists(mapper_output_dir):
        os.makedirs(mapper_output_dir)

    with open(os.path.join(mapper_output_dir, names['mapper_name'] + '.java'), r'w') as f:
        f.write(response)


def generate_dao(table_columns):
    """
    生成dao实现类
    :param table_columns: 表结构列数详细信息
    :return:
    """
    """
        生成mapper类
        :param table_columns: 表结构列数详细信息
        :return:
        """
    entity_parser = EntityParser(table_columns)
    # 转换为java中的字段
    columns = entity_parser.parse()
    # 获取类名
    table_name_parser = TableNameParser(table)
    names = table_name_parser.get_all_names()
    primary_keys = ', '.join(
        [column['property_type'] + ' ' + column['property'] for column in columns if column['is_primary'] is True])
    primary_keys_exclude_type = ', '.join(
        [column['property'] for column in columns if column['is_primary'] is True])

    # 获取模板文件
    template = env.get_template("dao/dao.jinja2")
    response = template.render(columns=columns, names=names, primary_keys=primary_keys
                               , primary_keys_exclude_type=primary_keys_exclude_type)

    mapper_output_dir = os.path.join(output_dir, *config.dao_package.split('.'))
    if not os.path.exists(mapper_output_dir):
        os.makedirs(mapper_output_dir)

    with open(os.path.join(mapper_output_dir, names['dao_name'] + '.java'), r'w') as f:
        f.write(response)


def generate_dao_interface(table_columns):
    """
    生成dao接口
    :param table_columns: 表结构列数详细信息
    :return:
    """
    entity_parser = EntityParser(table_columns)
    # 转换为java中的字段
    columns = entity_parser.parse()
    # 获取类名
    table_name_parser = TableNameParser(table)
    names = table_name_parser.get_all_names()
    primary_keys = ', '.join(
        [column['property_type'] + ' ' + column['property'] for column in columns if column['is_primary'] is True])

    # 获取模板文件
    template = env.get_template("dao/dao.interface.jinja2")
    response = template.render(columns=columns, names=names, primary_keys=primary_keys)

    mapper_output_dir = os.path.join(output_dir, *config.dao_interface_package.split('.'))
    if not os.path.exists(mapper_output_dir):
        os.makedirs(mapper_output_dir)

    with open(os.path.join(mapper_output_dir, names['dao_interface_name'] + '.java'), r'w') as f:
        f.write(response)


def generate_entity(table_columns):
    """
    根据表列信息生成Java实体
    :param table_columns: 表结构列数详细信息
    :return:
    """
    entity_parser = EntityParser(table_columns)
    # 转换为java中的字段
    java_fields = entity_parser.parse()
    # 获取类名
    table_name_parser = TableNameParser(table)
    all_names = table_name_parser.get_all_names()
    # 获取模板文件
    template = env.get_template("dao/entity.jinja2")
    response = template.render(java_fields=java_fields, names=all_names)

    entity_output_dir = os.path.join(output_dir, *config.entity_package.split('.'))
    if not os.path.exists(entity_output_dir):
        os.makedirs(entity_output_dir)

    with open(os.path.join(entity_output_dir, all_names['entity_name'] + '.java'), r'w') as f:
        f.write(response)


if __name__ == "__main__":
    # 获取当前所在目录
    current_dir = os.path.dirname(__file__)
    # 文件输出目录
    output_dir = os.path.join(current_dir, "output")
    # 清空输出文件夹
    shutil.rmtree(output_dir)

    # 根据FileSystemLoader获取Environment
    env = Environment(loader=FileSystemLoader(os.path.join(current_dir, 'template')))

    try:
        # 打开数据库连接
        db = pymysql.connect(host=dbconfig.db_host, database=dbconfig.database, user=dbconfig.db_user, password=dbconfig.db_password)
        # 创建cursor
        cursor = db.cursor()
        # 循环处理每个数据库表
        for table in dbconfig.tables.split(","):
            # 使用execute执行sql
            cursor.execute("desc " + table)
            rows = cursor.fetchall()
            # 生成Java实体
            generate_entity(rows)
            generate_mapper(rows)
            generate_dao(rows)
            generate_dao_interface(rows)
            generate_mapper_xml(rows)

    finally:
        # 关闭数据库
        db.close()