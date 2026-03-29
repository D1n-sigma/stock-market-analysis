import pandas as pd
import os

stocks = ["AAPL", "GOOGL", "TSLA", "MSFT"]

for ticker in stocks:
    print(f"Calculating indicators for {ticker}...")
    
    df = pd.read_csv(f"data/processed/{ticker}_clean.csv")
    df["Date"] = pd.to_datetime(df["Date"])

    # Moving Average 20 & 50 Days
    df["MA20"] = df["close"].rolling(window=20).mean()
    df["MA50"] = df["close"].rolling(window=50).mean()

    # RSI (relative strength index)
    delta = df["close"].diff()
    gain = delta.where(delta > 0, 0).rolling(window=14).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    # MACD (moving average convergence divergence)
    df["EMA12"] = df["close"].ewm(span=12, adjust=False).mean()
    df["EMA26"] = df["close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = df["EMA12"] - df["EMA26"]
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    # Save
    df.to_csv(f"data/processed/{ticker}_indicators.csv", index=False)
    print(f"{ticker} indicators calculated and saved!")

print(f"\nAll indicators successfully calculated and saved.")   