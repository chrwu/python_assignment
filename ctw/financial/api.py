from fastapi import FastAPI, Depends, Request
from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from model import engine, FinancialData, SessionLocal
from typing import Optional
from get_raw_data import ingest_raw_data_pg

import datetime
import model
import schemas
#import requests


app = FastAPI(title="CTW")
model.Base.metadata.create_all(bind=engine)
TODAY = datetime.date.today().strftime("%Y-%m-%d")
two_weeks_ago = datetime.date.today() - datetime.timedelta(days=13)
DATE_TWO_WEEKS_AGO = two_weeks_ago.strftime("%Y-%m-%d")
try:
   ingest_raw_data_pg()
except:
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    pass


@app.get("/financial_data", response_model=schemas.Data)
def get_financial_data(req: Request,
                       start_date: Optional[str] = DATE_TWO_WEEKS_AGO, end_date: Optional[str] = TODAY,
                       symbol: Optional[str] = 'AAPL', limit: Optional[int] = 5, page: Optional[int] = 0,
                       db: Session = Depends(get_db)):
    offset = limit * page
    query_count = select(model.FinancialData)

    query = select(model.FinancialData).filter(
        and_(model.FinancialData.date >= datetime.datetime.strptime(start_date, '%Y-%m-%d'),
             model.FinancialData.date <= datetime.datetime.strptime(end_date, '%Y-%m-%d')),
        model.FinancialData.symbol == symbol
    )
    with db.begin():
        db_count = db.execute(query_count)
        count = len([d.__dict__ for d in db_count.scalars().all()])
        db_data = db.execute(query)
        db_data = [d.__dict__ for d in db_data.scalars().all()]
        pages = 0 if count % limit == 0 else 1
        pages += count / limit

        return {
            "data": db_data,
            "pagination": {"count": count, "page": page, "limit": limit, "pages": pages},
            "info": {"error": ''}
        }


@app.get("/statistics", response_model=schemas.Statistics)
def get_financial_data(req: Request,
                       start_date: str, end_date: str, symbol: str,
                       db: Session = Depends(get_db)):
    dt_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    dt_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    query = select(model.FinancialData).filter(
        and_(model.FinancialData.date >= dt_start_date, model.FinancialData.date <= dt_end_date),
        model.FinancialData.symbol == symbol
    )
    with db.begin():
        db_data = db.execute(query)
        avg_open_price, avg_close_price, avg_vol = 0.0, 0.0, 0
        #_start_date, _end_date = datetime.datetime.date(dt_end_date), datetime.datetime.date(dt_start_date)
        n = 0
        for d in db_data.scalars().all():
            avg_open_price += d.__dict__['open_price']
            avg_close_price += d.__dict__['close_price']
            avg_vol += d.__dict__['volume']
            n += 1
            
        if n > 0:
            avg_open_price /= n
            avg_close_price /= n
            avg_vol /= n

        return {
            "data": {
                "start_date": dt_start_date,
                "end_date": dt_end_date,
                "symbol": symbol,
                "average_daily_open_price": avg_open_price,
                "average_daily_close_price": avg_close_price,
                "average_daily_volume": int(avg_vol)
            },
            "info": {"error": ''}
        }


@app.post('/ingest_data')
def get_raw_data(req: Request,
                 symbol: str = 'TEST',
                 date: str = '2023-07-03',
                 open_price: float = 100.0,
                 close_price: float =200.0,
                 volume: int = 1000,
                 db: Session = Depends(get_db)):

    test_data = FinancialData(
        symbol=symbol,
        date=datetime.datetime.strptime(date, '%Y-%m-%d'),
        open_price=open_price,
        close_price=close_price,
        volume=volume)
    db.add(test_data)
    db.commit()



