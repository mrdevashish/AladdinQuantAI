import os
from datetime import datetime

# Try DuckDB first
try:
    import duckdb
    DB_TYPE = "duckdb"
except:
    import sqlite3
    DB_TYPE = "sqlite"

class TickDB:

    def __init__(self):

        if DB_TYPE == "duckdb":

            self.db = duckdb.connect("database/ticks.duckdb")

            self.db.execute("""
            CREATE TABLE IF NOT EXISTS ticks(
                ts TIMESTAMP,
                symbol VARCHAR,
                price DOUBLE
            )
            """)

        else:

            self.db = sqlite3.connect("database/ticks.sqlite")

            self.db.execute("""
            CREATE TABLE IF NOT EXISTS ticks(
                ts TEXT,
                symbol TEXT,
                price REAL
            )
            """)

    def insert(self,symbol,price):

        now = datetime.utcnow()

        if DB_TYPE == "duckdb":

            self.db.execute(
                "INSERT INTO ticks VALUES (?,?,?)",
                [now,symbol,price]
            )

        else:

            self.db.execute(
                "INSERT INTO ticks VALUES (?,?,?)",
                [str(now),symbol,price]
            )

            self.db.commit()
