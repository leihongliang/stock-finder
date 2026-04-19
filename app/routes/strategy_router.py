from fastapi import APIRouter, HTTPException
from app.models.stock import StrategyValidationRequest
from app.services.stock_service import StockService
import datetime
from app.services.strategies import validate_513_strategy as validate_513

router = APIRouter(prefix="/api/stocks", tags=["stocks-strategy"])
stock_service = StockService()

@router.post("/strategy/validate")
def validate_strategy(request: StrategyValidationRequest):
    """根据策略从历史数据中找到符合的股票及其时间段区间，并验证之后几天的股票涨幅，计算策略的正确率
    
    目前支持的策略：
    - strategy1: 至少连续上涨≥4天（允许夹一根小阴线），出现放量大阳线，后续3天不跌破异动阳线的开盘价
    - strategy_513: 513战法，可自定义连续上涨天数和后续验证天数
    - rising_surge_3: 513战法的英文名称
    """
    try:
        # 验证策略
        result = stock_service.validate_strategy(
            request.strategy_name,
            request.start_date,
            request.end_date
        )
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器内部错误: {str(e)}")

@router.post("/strategy/validate/513")
def validate_513_strategy(request: StrategyValidationRequest, consecutive_days: int = 4, verification_days: int = 3):
    """验证513战法（可自定义连续上涨天数和后续验证天数）
    
    Args:
        request: 策略验证请求
        consecutive_days: 连续上涨天数，默认4天
        verification_days: 后续验证天数，默认3天
    """
    try:
        # 设置默认时间范围为近7天
        if not request.start_date or not request.end_date:
            end_date = datetime.date.today()
            start_date = end_date - datetime.timedelta(days=7)
            request.start_date = start_date.strftime("%Y-%m-%d")
            request.end_date = end_date.strftime("%Y-%m-%d")
        
        # 调用策略验证函数
        result = validate_513(
            stock_service,
            request.start_date,
            request.end_date,
            consecutive_days,
            verification_days,
            request.stock_codes
        )
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器内部错误: {str(e)}")