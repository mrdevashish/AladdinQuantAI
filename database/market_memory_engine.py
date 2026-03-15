import sqlite3
from fyers_wrapper.data.historical import get_history

DB="database/market_memory.sqlite"

class MarketMemory:

    def __init__(self):

        self.db = sqlite3.connect(DB)

        self.db.execute("""
        CREATE TABLE IF NOT EXISTS candles(
        symbol TEXT,
        ts INTEGER,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL
        )
        """)

    def store_history(self,symbol):

        print("Fetching candles for",symbol)

        data = get_history(symbol)

        candles = data["candles"]

        for c in candles:

            self.db.execute(
            "INSERT INTO candles VALUES (?,?,?,?,?,?,?)",
            (symbol,*c)
            )

        self.db.commit()

        print("Stored",len(candles),"candles")
