import duckdb
import os
from datetime import datetime

DB_FILE = "database/market_ticks.duckdb"

class TickStore:

    def __init__(self):
        self.con = duckdb.connect(DB_FILE)

        self.con.execute("""
        CREATE TABLE IF NOT EXISTS ticks(
            time TIMESTAMP,
            symbol VARCHAR,
            ltp DOUBLE,
            volume DOUBLE
        )
        """)

    def insert_tick(self,symbol,ltp,volume=0):

        now = datetime.utcnow()

        self.con.execute(
            "INSERT INTO ticks VALUES (?,?,?,?)",
            [now,symbol,ltp,volume]
        )

    def close(self):
        self.con.close()
