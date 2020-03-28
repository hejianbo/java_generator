from config.base_config import BaseConfig


class DalConfig(BaseConfig):
    def __init__(self, config):
        super().__init__(config)
        self.dal_package = self.base_package + config.get("template_dal", "dal_package")
        self.dao_interface_package = self.base_package
        self.dao_package = self.dal_package + config.get("template_dal", "dao_package")
        self.mapper_package = self.dal_package + config.get("template_dal", "mapper_package")
        self.entity_package = self.dal_package + config.get("template_dal", "entity_package")
        self.entity_suffix = config.get("template_dal", "entity_suffix")
        self.batch_insert_ignore_fields = config.get("template_dal", "batch_insert_ignore_fields")
        self.batch_update_ignore_fields = config.get("template_dal", "batch_update_ignore_fields")

