import os

from jinja2 import Environment, FileSystemLoader

from myparser import EntityParser, TableNameParser


class TemplateParser(object):
    def __init__(self, current_dir, output_dir, service_config, dal_config):
        self.env = Environment(loader=FileSystemLoader(os.path.join(current_dir, 'template')))
        self.output_dir = output_dir
        self.service_config = service_config
        self.dal_config = dal_config

    def render2(self, template_item):
        entity_parser = EntityParser(template_item.table_columns)
        # 转换为java中的字段
        columns = entity_parser.parse()
        # 获取类名
        table_name_parser = TableNameParser(template_item.table_name)
        all_names = table_name_parser.get_all_names()

        template = self.env.get_template(template_item.template_path)
        response = template.render(columns=columns, names=all_names)

        entity_output_dir = os.path.join(self.output_dir, *template_item.package_name.split('.'))
        if not os.path.exists(entity_output_dir):
            os.makedirs(entity_output_dir)

        with open(os.path.join(entity_output_dir, all_names[template_item.output_filename] + template_item.output_file_type), r'w', encoding="utf-8") as f:
            f.write(response)
