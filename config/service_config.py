from config.base_config import BaseConfig


class ServiceConfig(BaseConfig):
    def __init__(self, config):
        super().__init__(config)
        self.service_interface_package = self.base_package + config.get("template_service", "service_interface_package")
        self.service_package = self.base_package + config.get("template_service", "service_package")
        self.service_bo_package = self.base_package + config.get("template_service", "service_bo_package")
        self.service_bo_suffix = config.get("template_service", "service_bo_suffix")
