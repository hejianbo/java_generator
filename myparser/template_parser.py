import os
from jinja2 import Environment, FileSystemLoader
from myparser import EntityParser, TableNameParser
import config.basic_config as config


class TemplateParser(object):
    def __init__(self, current_dir, output_dir):
        self.env = Environment(loader=FileSystemLoader(os.path.join(current_dir, 'template')))
        self.output_dir = output_dir

    def render(self, table, table_columns, template_path, package_name, output_filename, file_type):
        entity_parser = EntityParser(table_columns)
        # 转换为java中的字段
        columns = entity_parser.parse()
        # 获取类名
        table_name_parser = TableNameParser(table)
        all_names = table_name_parser.get_all_names()

        template = self.env.get_template(template_path)
        response = template.render(columns=columns, names=all_names)

        entity_output_dir = os.path.join(self.output_dir, *package_name.split('.'))
        if not os.path.exists(entity_output_dir):
            os.makedirs(entity_output_dir)

        with open(os.path.join(entity_output_dir, all_names[output_filename] + file_type), r'w', encoding="utf-8") as f:
            f.write(response)
