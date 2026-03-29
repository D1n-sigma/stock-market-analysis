import pandas  as pd
import os

# Daftar saham
stocks = ["AAPL", "GOOGL", "TSLA", "MSFT"]

# Folder proses 
os.makedirs("data/processed", exist_ok=True)

for ticker in stocks:
    print(f"Cleaning {ticker}...")

    # Baca file raw
    df= pd.read_csv(f"data/raw/{ticker}.csv", skiprows=[1,2])

    # Rename kolom
    df.columns = ["Date", "close", "High", "Low", "Open", "Volume"]

    # Delete baris kosong
    df.dropna(inplace=True)

    # Convert kolom Date ke format datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Urutkan berdasarkan tanggal
    df.sort_values("Date", inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # save to processed
    df.to_csv(f"data/processed/{ticker}_clean.csv", index=False)
    print(f"{ticker} cleaned and saved!")

    print(f"\nAll data successfully cleaned and saved.")