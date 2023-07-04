from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class MsgResponse(BaseModel):
    message: str
    id: Optional[str] = None


class FinData(BaseModel):
    symbol: str
    date: date
    open_price: float
    close_price: float
    volume: int


class Pagination(BaseModel):
    count: int
    page: int
    limit: int
    pages: int


class Info(BaseModel):
    error: str = ''


class Data(BaseModel):
    data: List[FinData]
    pagination: Pagination
    info: Info


class AvgFinData(BaseModel):
    start_date: date
    end_date: date
    symbol: str
    average_daily_open_price: float
    average_daily_close_price: float
    average_daily_volume: int


class Statistics(BaseModel):
    data: AvgFinData
    info: Info