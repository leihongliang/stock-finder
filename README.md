# 📈 Stock Strategy Backtester - A股股票策略回测系统

## 📋 项目简介

Stock Strategy Backtester 是一个基于 FastAPI 开发的 A 股股票策略回测系统，主要功能是根据交易策略回测历史数据，给出策略的量化数据，支持涨跌模式查询、股票数据更新等功能。

## ✨ 功能特性

- 📈 **策略回测**：根据交易策略回测历史数据，计算策略的正确率和收益率
- 🎯 **涨跌模式查询**：根据用户输入的涨跌模式，查找匹配的股票
- 📊 **股票数据更新**：支持从 AkShare 和 Tushare 获取最新的股票数据
- 🏢 **A股公司信息管理**：获取和更新 A 股公司基本信息
- 📅 **交易日历同步**：同步最新的交易日历数据
- 🔄 **每日自动更新**：提供每日更新接口，自动更新交易日历、公司信息和日K线数据

## 🛠️ 技术栈

- **后端框架**：FastAPI 🚀
- **数据处理**：Pandas 🐼
- **数据库**：MongoDB 📦
- **数据源**：AkShare、Tushare 📡
- **API文档**：Swagger UI、ReDoc 📖

## 📥 安装步骤

1. **克隆项目** 📁

```bash
git clone <项目地址>
cd stock-finder
```

2. **安装依赖** 📦

```bash
# 使用 pip
pip install -r requirements.txt

# 或使用 uv (推荐)
uv install
```

3. **配置数据库** ⚙️

在 `app/config/settings.py` 中配置 MongoDB 连接信息：

```python
# MongoDB 配置
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_DATABASE = "stock_data"
```

4. **启动服务** 🚀

```bash
python run.py
```

服务将在 `http://localhost:8000` 启动，可通过以下地址访问：
- Swagger UI: http://localhost:8000/docs 📖
- ReDoc: http://localhost:8000/redoc 📚

## 🔌 API 接口

### 1. 策略回测

**POST /api/stocks/strategy/validate**

根据策略从历史数据中找到符合的股票及其时间段区间，并验证之后几天的股票涨幅，计算策略的正确率和收益率。

请求体：
```json
{
  "strategy_name": "strategy1",
  "start_date": "2023-01-01",
  "end_date": "2023-12-31"
}
```

### 2. 涨跌模式查询

**POST /api/stocks/pattern**

根据涨跌模式查找匹配的股票。

请求体：
```json
{
  "pattern": "11101",
  "start_date": "2023-01-01",
  "end_date": "2023-12-31"
}
```

### 3. 刷新所有股票数据

**POST /api/stocks/refresh**

从数据源获取所有 A 股的近一年日K线数据并保存到数据库。

### 4. 更新单只股票数据

**POST /api/stocks/update**

更新指定股票的日K线数据。

请求体：
```json
{
  "stock_code": "600000",
  "start_date": "20230101",
  "end_date": "20231231",
  "data_source": "akshare"
}
```

### 5. 刷新 A 股公司信息

**POST /api/stocks/companies**

获取所有 A 股公司信息并存入数据库。

### 6. 获取沪港通/深港通股票列表

**GET /api/stocks/hsgt**

获取指定日期的沪港通/深港通股票列表。

查询参数：
- `trade_date`: 交易日期，格式为 "YYYYMMDD"（可选，默认使用当天日期）

### 7. 同步固定时间范围内的股票数据

**POST /api/stocks/sync-range**

同步指定时间范围内的股票数据到数据库。

请求体：
```json
{
  "start_date": "20230101",
  "end_date": "20231231",
  "stock_codes": ["600000", "600001"],
  "data_source": "tushare"
}
```

### 8. 同步交易日历数据

**POST /api/stocks/sync-calendar**

从 AkShare 获取 A 股交易日历数据，并保存到数据库。

### 9. 每日更新

**POST /api/stocks/daily-update**

执行每日更新操作，包括：
1. 更新交易日历到最新的一天
2. 更新新增的 A 股公司信息
3. 更新日K线到最新的一天

## 📁 项目结构

```
stock-finder/
├── app/
│   ├── config/           # 配置文件
│   ├── models/           # 数据模型
│   ├── repositories/     # 数据库操作
│   ├── routes/           # API路由
│   ├── services/         # 业务逻辑
│   │   └── data_sources/ # 数据源实现
│   ├── utils/            # 工具函数
│   └── main.py           # 应用入口
├── logs/                 # 日志文件
├── pyproject.toml        # 项目配置
├── run.py                # 运行脚本
└── README.md             # 项目说明
```

## 🧩 主要功能模块

### 1. 策略模块 (strategies) 🎯

实现了股票策略的回测逻辑，包括：
- strategy1: 4连阳 + 1根异常放量阳线 + 3天验证
- strategy2: 简单金叉策略

每个策略都会计算：
- 匹配模式数量
- 总案例数
- 成功案例数
- 策略正确率
- 5日、10日、20日涨幅

### 2. 股票服务 (StockService) 📈

负责处理股票相关的业务逻辑，包括：
- 股票数据的获取和保存
- 涨跌模式的生成和匹配
- 策略回测和验证
- 每日更新操作

### 3. 数据源 📡

支持从多个数据源获取股票数据：
- AkShare: 提供 A 股股票列表和日K线数据
- Tushare: 提供更详细的股票数据

### 4. 数据库操作 📦

支持 MongoDB 数据库：
- 存储股票价格数据
- 存储公司信息
- 存储交易日历数据

## 🔄 数据更新机制

### 手动更新

- **刷新所有股票数据**：通过 `/api/stocks/refresh` 接口
- **更新单只股票**：通过 `/api/stocks/update` 接口
- **刷新公司信息**：通过 `/api/stocks/companies` 接口
- **同步交易日历**：通过 `/api/stocks/sync-calendar` 接口

### 每日自动更新

通过 `/api/stocks/daily-update` 接口，执行以下操作：
1. 更新交易日历到最新的一天
2. 更新新增的 A 股公司信息
3. 更新日K线到最新的一天（最近10天）

## 📈 策略回测

系统支持回测以下策略：

### Strategy 1: 4连阳 + 1根异常放量阳线 + 3天验证

- **条件**：至少连续上涨≥4天（允许夹一根小阴线），出现放量大阳线，后续3天不跌破异动阳线的开盘价
- **回测结果**：
  - 匹配模式数量
  - 总案例数
  - 成功案例数
  - 策略正确率
  - 5日、10日、20日涨幅

### Strategy 2: 简单金叉策略

- **条件**：MA5上穿MA20形成金叉
- **回测结果**：
  - 匹配模式数量
  - 总案例数
  - 成功案例数
  - 策略正确率
  - 5日、10日、20日涨幅

## ⚠️ 注意事项

1. **数据获取限制**：AkShare 和 Tushare 都有 API 调用限制，请合理使用
2. **数据库配置**：请确保 MongoDB 服务正常运行
3. **首次使用**：首次使用时需要先同步交易日历和公司信息
4. **性能优化**：处理大量股票数据时可能会比较耗时，请耐心等待
5. **日志查看**：详细的操作日志保存在 `logs/stock_finder.log` 文件中

## 🚀 扩展建议

1. **添加更多策略**：可以在 `strategies.py` 中添加更多的股票策略
2. **支持更多数据源**：可以扩展 `data_sources` 目录，添加更多的数据源
3. **添加数据可视化**：可以集成前端框架，添加数据可视化功能
4. **添加用户认证**：可以添加用户认证机制，限制 API 访问
5. **添加定时任务**：可以配置定时任务，自动执行每日更新操作

## 📄 许可证

MIT
