# 展品档案元数据治理

这里是数字档案治理服务的起始代码。展品标识、原始元数据和规范化结果需要保持来源可追溯，导入流程与规则校验应通过应用层衔接。

## 目录约定

- `src/archive_governance/domain.py`：档案和导入批次的基础类型。
- `src/archive_governance/`：规则、批处理和数据库适配器。
- `tests/`：导入与校验的自动化检查。

## 运行

Python 3.11+ 可直接运行 `python -m unittest discover -s tests`。数据库文件放在运行目录之外或由配置指定。
