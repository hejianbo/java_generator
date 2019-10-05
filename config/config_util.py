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

    @staticmethod
    def get_config_by_full_path(full_path):
        conf = configparser.ConfigParser()
        conf.read(full_path, "utf-8")
        return conf
