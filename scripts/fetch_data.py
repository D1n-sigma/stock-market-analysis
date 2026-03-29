import yfinance as yf
import os

#daftar saham yang saya analisa
stocks = ["AAPL", "GOOGL", "TSLA", "MSFT"]

# Periode data
start_date = "2022-01-01"
end_date = "2024-01-01"

os.makedirs("data/raw", exist_ok=True)

# Down and save for every stock
for ticker in stocks:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f"data/raw/{ticker}.csv")
    print(f"{ticker} saved!")

print("\nAll data successfully downloaded.")