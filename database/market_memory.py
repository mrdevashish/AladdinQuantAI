import duckdb

DB="database/memory.duckdb"

class MarketMemory:

    def __init__(self):

        self.con=duckdb.connect(DB)

        self.con.execute("""
        CREATE TABLE IF NOT EXISTS candles(
        symbol VARCHAR,
        ts BIGINT,
        open DOUBLE,
        high DOUBLE,
        low DOUBLE,
        close DOUBLE,
        volume DOUBLE
        )
        """)

    def store(self,data):

        for c in data:

            self.con.execute(
            "INSERT INTO candles VALUES (?,?,?,?,?,?,?)",
            ["NIFTY",*c]
            )
