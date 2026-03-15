from database.market_memory_engine import MarketMemory

mm = MarketMemory()

symbols = [
"NSE:NIFTY50-INDEX",
"NSE:NIFTYBANK-INDEX"
]

for s in symbols:

    mm.store_history(s)
