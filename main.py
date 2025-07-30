import yfinance as yf
import pandas as pd
import numpy as np

# 🔹 List of stocks/crypto to scan
tickers = ["AAPL", "TSLA", "NVDA", "BTC-USD", "ETH-USD", "SOL-USD", "QQQM", "HYDR", "COIN", "LTC-USD", "IBIT", "IWM", "ETHE", "MSTR", "META", "AMZN", "NFLX", "ERIC", "GOOGL", "INTC", "AMD", "DELL", "ARM", "HPE", "T", "VZ", "EVLV", "GME", "GPC", "DHI", "HD", "O", "VST", "ISRG"]


def scan_stock(ticker):
    """Scan stocks to find opperuntinies """
    # Get 1 year of data
    data = yf.download(ticker, period="1y", progress=False)

    # Ensure we have enough data
    if data.empty or len(data) < 200:
        return  # Skip if not enough historical data

    # 🔹 Calculate Moving Averages
    data["SMA_50"] = data["Close"].rolling(window=50).mean()
    data["SMA_200"] = data["Close"].rolling(window=200).mean()

    # 🔹 Calculate RSI
    delta = data["Close"].diff()
    gain = np.where(delta > 0, delta, 0).flatten()
    loss = np.where(delta < 0, -delta, 0).flatten()
    avg_gain = pd.Series(gain, index=data.index).rolling(window=14).mean()
    avg_loss = pd.Series(loss, index=data.index).rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))

    # 🔹 Calculate MACD
    data["MACD"] = data["Close"].ewm(span=12).mean() - data["Close"].ewm(span=26).mean()
    data["Signal"] = data["MACD"].ewm(span=9).mean()

    # 🔹 Identify Last Data Points
    try:
        last_close = data["Close"].dropna().iloc[-1]
        last_sma_200 = data["SMA_200"].dropna().iloc[-1]
        last_rsi = data["RSI"].dropna().iloc[-1]
        last_macd = data["MACD"].dropna().iloc[-1]
        last_signal = data["Signal"].dropna().iloc[-1]
    except IndexError:
        return  # Skip if any missing data

    # Ensure values are scalars
    last_close = last_close if isinstance(last_close, (int, float, np.number)) else last_close.iloc[-1]
    last_sma_200 = last_sma_200 if isinstance(last_sma_200, (int, float, np.number)) else last_sma_200.iloc[-1]

    # 🔥 Trading Conditions
    conditions = []

    if last_close < last_sma_200:
        conditions.append("📉 Below 200-SMA (Potential Buy)")

    if last_rsi < 30:
        conditions.append("🔥 RSI Oversold (Potential Reversal)")

    if last_macd > last_signal:
        conditions.append("✅ MACD Bullish Crossover")

    # 🔹 Display results **only if two or more conditions are met**
    if len(conditions) >= 2:
        print(f"\n🔍 {ticker} Strong Swing Trade Opportunity:")
        for condition in conditions:
            print(f"   - {condition}")


# 🔹 Run scanner on all tickers
print("📡 Running Market Scanner...")
for ticker in tickers:
    scan_stock(ticker)
