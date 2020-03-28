from config.config_util import ConfigUtil


class TemplateItemFactory(object):
    def __init__(self, conf, template_path):
        self.template_conf = ConfigUtil.get_config_by_full_path(template_path)
        self.conf = conf

    def get_template_items(self):
        enable_templates = self.conf.get("template", "enable_templates")
        template_items = []
        for template in enable_templates.split(","):
            template = str.strip(template)
            if self.template_conf.has_section(template):
                template_item = {
                    "template_path": self.template_conf.get(template, "template_path"),
                    "output_file_type": self.template_conf.get(template, "file_type"),
                    "output_filename": self.template_conf.get(template, "template_name"),
                    "output_dir": self.template_conf.get(template, "output_dir"),
                }
                template_items.append(template_item)
        return template_items

