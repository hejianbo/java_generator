class EntityParser(object):
    def __init__(self, columns):
        self.columns = columns

    def parse(self):
        """
        0: 列名称
        1: 类型
        2: 是否可空
        3: Key: PRI 主键, 可以有多个主键
        4: 默认值
        5: Extra
        :return:
        """
        result = []
        for column in self.columns:
            field_name = column[0]
            field_type = column[1].lower()
            result.append((EntityParser.get_class_type(field_type), EntityParser.get_class_name(field_name)))
        return result

    @staticmethod
    def get_class_name(field_name):
        """
        将数据库名称转换为Java对应的属性名称
        :param field_name: 数据库字段名称
        :return: java驼峰命名的名称
        """

        # 首先检测是否带下划线, 如果没有则直接返回
        if '_' not in field_name:
            return field_name
        words = field_name.split('_')
        first_word = words[0]
        other_words = words[1:]

        return first_word + ''.join([word.capitalize() for word in other_words])

    @staticmethod
    def get_class_type(field_type):
        """
        根据数据库类型获取Java对应的类型
        :param field_type: 数据库类型
        :return: Java类型
        """

        if field_type.startswith('tinyint'):
            return 'Boolean'
        if field_type.startswith('smallint'):
            return 'Integer'
        if field_type.startswith('int'):
            return "Integer"
        if field_type.startswith('bigint'):
            return "Long"
        if field_type.startswith('float'):
            return "Float"
        if field_type.startswith('double'):
            return "Double"
        if field_type.startswith('decimal'):
            return "BigDecimal"
        if field_type.startswith('varchar'):
            return 'String'
        if field_type.startswith('char'):
            return 'String'
        if field_type.startswith('text'):
            return 'String'
        if field_type.startswith('timestamp'):
            return 'Date'
        if field_type.startswith('date'):
            return 'Date'

        raise Exception("不支持的数据库型: ", field_type)
