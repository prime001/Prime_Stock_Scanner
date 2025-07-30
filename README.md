# 📈 SwingTradeScanner – AI-Enhanced Market Signal Screener

**SwingTradeScanner** is a Python-based scanner that analyzes top stocks and crypto assets for potential swing trading opportunities using key technical indicators: **200-day SMA**, **RSI**, and **MACD**. It scans a curated list of assets and identifies strong trade setups with minimal noise.

---

## 🚀 Features

- ✅ **200-SMA Crossover Check**  
  Detects assets trading below their long-term trend — potential value entry points.

- 🔥 **RSI Oversold Detection**  
  Flags assets with RSI below 30, often signaling a potential bounce or reversal.

- 📊 **MACD Bullish Crossover Signal**  
  Identifies early momentum shifts with MACD/Signal crossovers.

- 🧠 **Multi-Factor Filter**  
  Only prints results when **2 or more bullish signals** align — reducing false positives.

- 💰 Supports **stocks & crypto** (via Yahoo Finance ticker format)

---

## 🔧 Technical Indicators Used

- **SMA 200**: Long-term moving average  
- **RSI (14)**: Relative Strength Index  
- **MACD & Signal Line**: Momentum crossover detection

---

## 🧠 Example Output

```bash
📡 Running Market Scanner...

🔍 NVDA Strong Swing Trade Opportunity:
   - 📉 Below 200-SMA (Potential Buy)
   - ✅ MACD Bullish Crossover

🔍 ETH-USD Strong Swing Trade Opportunity:
   - 🔥 RSI Oversold (Potential Reversal)
   - ✅ MACD Bullish Crossover
