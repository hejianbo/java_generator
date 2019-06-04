base_package = "jwms"

# 配置包结构
dao_interface_package = base_package + ""
dao_package = dao_interface_package + ".impl"
mapper_package = dao_interface_package + ".dal"
entity_package = dao_interface_package + ".entity"
entity_suffix = "PO"
table_prefix = ""

service_package = base_package

# 代码输出根路径
output_dir = "/home/jianbo/output"
