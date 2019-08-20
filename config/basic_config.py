base_package = "com.oyo.scm.prediction"

dal_package = base_package + ".dal";

# DAL层配置
dao_interface_package = dal_package + ""
dao_package = dao_interface_package + ".impl"
mapper_package = dao_interface_package + ".impl.mapper"
entity_package = dao_interface_package + ".po"
entity_suffix = "PO"
table_prefix = ""

# 服务层配置
service_interface_package = base_package + ".core.service"
service_bo_package = service_interface_package + ".bo"
service_bo_suffix = "BO"
service_package = service_interface_package + ".impl"


# 代码输出根路径
output_dir = "/home/jianbo/output"
