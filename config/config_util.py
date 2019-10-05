import configparser
import os


class ConfigUtil(object):
    @staticmethod
    def get_config(directory, file):
        # 加载config.ini配置文件
        conf = configparser.ConfigParser()
        config_file_path = os.path.join(directory, file)
        conf.read(config_file_path, "utf-8")
        return conf
