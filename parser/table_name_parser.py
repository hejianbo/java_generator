import config.basic_config as config


class TableNameParser(object):

    def __init__(self, table_name):
        self.table_name = table_name
        # 首先将表名的前缀给去掉
        table_name = table_name.lstrip(config.table_prefix)

        words = table_name.split("_")
        if len(words) == 1:
            # 单词首字母全大写
            self.variable_name = words[0]
            # 除第一个单词外所有首字母大写
            self.class_name = words[0].capitalize()
        else:
            self.variable_name = words[0] + ''.join([word.capitalize() for word in words[1:]])
            self.class_name = ''.join([word.capitalize() for word in words])

    def get_entity_name(self):
        return self.class_name + config.entity_suffix

    def get_entity_variable(self):
        return self.variable_name + config.entity_suffix

    def get_mapper_name(self):
        return self.class_name + "Mapper"

    def get_mapper_variable(self):
        return self.variable_name + "Mapper"

    def get_dao_name(self):
        return self.class_name + "DaoImpl"

    def get_dao_variable(self):
        return self.variable_name + "DaoImpl"

    def get_dao_interface_name(self):
        return "I" + self.class_name + "Dao"

    def get_dao_interface_variable(self):
        return self.variable_name + "Dao"

    def get_service_name(self):
        return self.class_name + "ServiceImpl"

    def get_all_names(self):
        """
        获取所有需要解析出来的名称
        :return:
        """
        return {
            "table_name": self.table_name,
            "entity_name": self.get_entity_name(),
            "entity_package_name": config.entity_package,
            "entity_variable_name": self.get_entity_variable(),
            "dao_name": self.get_dao_name(),
            "dao_variable_name": self.get_dao_variable(),
            "dao_package_name": config.dao_package,
            "dao_interface_name": self.get_dao_interface_name(),
            "dao_interface_variable_name": self.get_dao_interface_variable(),
            "dao_interface_package_name": config.dao_interface_package,
            "mapper_name": self.get_mapper_name(),
            "mapper_package_name": config.mapper_package,
            "mapper_variable_name": self.get_mapper_variable(),
        }
