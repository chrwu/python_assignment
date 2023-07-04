import datetime
import requests
import sqlite3
import os

from model import SessionLocal, FinancialData
from sqlalchemy.orm import Session


company = ["IBM", "AAPL"]

def fetch_raw_data():
    yesterday = datetime.date.today() - datetime.timedelta(days=13)
    target_day = yesterday.strftime("%Y-%m-%d")
    fin_data = {}
    for c in company:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={c}&apikey={os.environ["API_KEY"]}'
        r = requests.get(url)
        data = r.json()
        result = []
        for k in data['Weekly Time Series'].keys():
            if k >= target_day:
                tmp = {
                    "symbol": c,
                    "date": k,
                    "open_price": data['Weekly Time Series'][k]['1. open'],
                    "close_price": data['Weekly Time Series'][k]['4. close'],
                    "volume": data['Weekly Time Series'][k]['5. volume']
                }
                result.append(tmp)
        fin_data[c] = result
    return fin_data


def ingest_raw_data_pg():
    db: Session = SessionLocal()
    raw_data = fetch_raw_data()
    for _, data in raw_data.items():
        for d in data:
            fin_data = FinancialData(
                symbol=d["symbol"],
                date=d["date"],
                open_price=d["open_price"],
                close_price=d["close_price"],
                volume=d["volume"])
            db.add(fin_data)
    db.commit()
    db.close()



if __name__ == '__main__':
    ingest_raw_data_pg()