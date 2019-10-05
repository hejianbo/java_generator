class TemplateItem(object):
    def __init__(self, table_name, table_columns, template_path, output_dir, output_filename, output_file_type):
        self.table_name = table_name
        self.table_columns = table_columns
        self.template_path = template_path
        self.output_dir = output_dir
        self.output_filename = output_filename
        self.output_file_type = output_file_type
