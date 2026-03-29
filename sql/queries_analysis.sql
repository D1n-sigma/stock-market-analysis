-- 1 Highly stock with available closing price 
SELECT ticker, Round(AVG(close), 2) AS avg_close_price
FROM stocks
GROUP BY ticker
GROUP BY avg_close DESC;

-- 2 Daily trade volume highest / stock
SELECT ticker, date, MAX(volume) AS max_volume
FROM stocks
GROUP BY ticker;

-- 3 Buy signal (RSI Under 30)
SELECT ticker, date, close, rsi
FROM stocks
WHERE rsi < 30
ORDER BY ticker, date;

-- 4 Benchmark return monthly
SELECT ticker,
    STFRFT(date, 'start of month') AS month,
    (MAX(close) - MIN(close)) / MIN(close) * 100 AS monthly_return
FROM stocks
GROUP BY ticker, month
ORDER BY ticker, month;