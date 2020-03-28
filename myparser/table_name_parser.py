class TableNameParser(object):

    def __init__(self, table_name, service_config, dal_config):
        self.table_name = table_name
        self.service_config = service_config
        self.dal_config = dal_config
        # 首先将表名的前缀给去掉
        table_name = table_name.lstrip(self.dal_config.table_prefix)

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
        return self.class_name + self.dal_config.entity_suffix

    def get_entity_variable(self):
        return self.variable_name + self.dal_config.entity_suffix

    def get_mapper_name(self):
        return self.class_name + "Mapper"

    def get_mapper_variable(self):
        return self.variable_name + "Mapper"

    def get_dao_name(self):
        return self.class_name + "Dao"

    def get_dao_variable(self):
        return self.variable_name + "Dao"

    def get_dao_interface_name(self):
        return "I" + self.class_name + "Dao"

    def get_dao_interface_variable(self):
        return self.variable_name + "Dao"

    def get_service_name(self):
        return self.class_name + "ServiceImpl"

    def get_service_interface_name(self):
        return "I" + self.class_name + "Service"

    def get_service_bo_name(self):
        return self.class_name + self.service_config.service_bo_suffix

    def get_all_names(self):
        """
        获取所有需要解析出来的名称
        :return:
        """
        return {
            "table_name": self.table_name,
            "entity_name": self.get_entity_name(),
            "entity_package_name": self.dal_config.entity_package,
            "entity_variable_name": self.get_entity_variable(),
            "dao_name": self.get_dao_name(),
            "dao_variable_name": self.get_dao_variable(),
            "dao_package_name": self.dal_config.dao_package,
            "dao_interface_name": self.get_dao_interface_name(),
            "dao_interface_variable_name": self.get_dao_interface_variable(),
            "dao_interface_package_name": self.dal_config.dao_interface_package,
            "mapper_name": self.get_mapper_name(),
            "mapper_package_name": self.dal_config.mapper_package,
            "mapper_variable_name": self.get_mapper_variable(),
            "service_name": self.get_service_name(),
            "service_interface_name": self.get_service_interface_name(),
            "service_bo_name": self.get_service_bo_name(),
            'service_bo_package_name': self.service_config.service_bo_package
        }
