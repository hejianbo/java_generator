class BaseConfig(object):
    def __init__(self, config):
        self.local_date_enable = config.get("template", "local_date_enable")
        self.base_package = config.get("template", "base_package")
        self.table_prefix = config.get("template", "table_prefix")
