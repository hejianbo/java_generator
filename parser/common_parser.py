class CommonParser(object):
    @staticmethod
    def get_class_name(table_name):
        return ''.join([word.capitalize() for word in table_name.split('_')])
