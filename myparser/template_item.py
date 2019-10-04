class TemplateItem(object):
    def __init__(self, table_name, table_columns, template_path, package_name, output_filename, output_file_type):
        self.table_name = table_name
        self.table_columns = table_columns
        self.template_path = template_path
        self.package_name = package_name
        self.output_filename = output_filename
        self.output_file_type = output_file_type
