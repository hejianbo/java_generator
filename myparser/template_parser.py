import os

from jinja2 import Environment, FileSystemLoader

from config.dal_config import DalConfig
from config.service_config import ServiceConfig
from myparser import EntityParser, TableNameParser


class TemplateParser(object):
    def __init__(self, current_dir, output_dir, conf):
        self.env = Environment(loader=FileSystemLoader(os.path.join(current_dir, 'template')))
        self.output_dir = output_dir
        self.dal_config = DalConfig(conf)
        self.service_config = ServiceConfig(conf)

    def render2(self, template_item):
        entity_parser = EntityParser(template_item.table_columns)
        # 转换为java中的字段
        columns = entity_parser.parse()
        # 获取所有相关名称

        # 名称解析: 如PO名称, Entity名称, Mapper名称等
        table_name_parser = TableNameParser(template_item.table_name, self.service_config, self.dal_config)
        all_names = table_name_parser.get_all_names()

        template = self.env.get_template(template_item.template_path)
        response = template.render(columns=columns, names=all_names)

        entity_output_dir = os.path.join(self.output_dir, template_item.package_name)
        if not os.path.exists(entity_output_dir):
            os.makedirs(entity_output_dir)

        with open(os.path.join(entity_output_dir, all_names[template_item.output_filename] + template_item.output_file_type), r'w', encoding="utf-8") as f:
            f.write(response)
