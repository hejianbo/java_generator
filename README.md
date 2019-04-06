# 根据MySQL表结构生成DAO层代码

## 生成的代码结构如下
默认生成的结构如下, 可以自己根据config.basic_config里的值进行修改调整
```
com.xxx.dao.IXxxDao
com.xxx.dao.impl.XxxDaoImpl
com.xxx.dao.impl.mapper.XxxMapper
com.xxx.dao.entity.XxxEntity
```

## 使用方式
1. 修改config.db_config里面的mysql数据库连接
2. 根据说明设置需要生成的表, 同时可以支持多表, 但需要以逗号分隔
3. 直接运行generator.py即可, 代码生成在当前目录的.output下面


本来想做得更通用，并把代码结构优化一下的，只是个人使用, 就没优化了。后续有时间再看考虑吧
