import pandas as pd
import sqlite3
import os

# Buat koneksi ke database SQLite
conn = sqlite3.connect("data/stocks.db")
cursor = conn.cursor()

# Buat tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    date TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    ma20 REAL,
    ma50 REAL,
    rsi REAL,
    macd REAL,
    signal REAL
)
""")

# Import data dari CSV ke database
stocks = ["AAPL", "GOOGL", "TSLA", "MSFT"]

for ticker in stocks:
    print(f"Loading {ticker} to database...")
    df = pd.read_csv(f"data/processed/{ticker}_indicators.csv")
    df["ticker"] = ticker
    df.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume",
        "MA20": "ma20",
        "MA50": "ma50",
        "RSI": "rsi",
        "MACD": "macd",
        "Signal": "signal"
    }, inplace=True)
    
    df[["ticker","date","open","high","low",
        "close","volume","ma20","ma50","rsi",
        "macd","signal"]].to_sql(
        "stocks", conn, 
        if_exists="append", 
        index=False
    )
    print(f"{ticker} loaded!")

conn.commit()
conn.close()
print("\nDatabase berhasil dibuat di data/stocks.db!")