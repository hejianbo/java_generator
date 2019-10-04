class DbConfig(object):
    def __init__(self, config):
        self.db_host = config.get("db", "db_host")
        self.db_name = config.get("db", "db_name")
        self.db_port = config.get("db", "db_port")
        self.db_user = config.get("db", "db_user")
        self.db_password = config.get("db", "db_password")
        self.db_tables = config.get("db", "db_tables")
