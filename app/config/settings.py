class Settings:
    """应用配置"""
    # 数据库配置
    DATABASE_TYPE = "mongodb"
    
    # MongoDB配置
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DATABASE = "stock_data"
    
    # 应用配置
    APP_NAME = "Stock Finder API"
    APP_VERSION = "0.1.0"

settings = Settings()
