# 展品档案元数据治理

这个 Spring Boot 工程为展品档案元数据治理保留领域层、接口层和外部存储边界。生产配置通过环境变量注入，仓库不会保存连接凭据。

## 开发

需要 JDK 17 和 Maven 3.9。执行 mvn test 运行基础测试，执行 mvn -DskipTests package 验证可打包。
