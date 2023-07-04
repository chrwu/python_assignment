from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Date, Integer, String, Float, UniqueConstraint
from config import settings


engine = create_engine(settings.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class FinancialData(Base):
    __tablename__ = "financial_data"

    #id = Column(String, primary_key=True, index=True)
    symbol = Column(String, primary_key=True, index=True)
    date = Column(Date, primary_key=True, index=True)
    open_price = Column(Float, index=False)
    close_price = Column(Float, index=False)
    volume = Column(Integer, index=False)
    UniqueConstraint(symbol, date)