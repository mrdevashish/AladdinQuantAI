import sqlite3

DB_FILE = "database/main.db"

class DBRouter:

    def __init__(self):

        self.db = sqlite3.connect(DB_FILE)

        self.db.execute("""
        CREATE TABLE IF NOT EXISTS ticks(
        ts INTEGER,
        symbol TEXT,
        price REAL
        )
        """)

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

        self.db.commit()

    def insert_tick(self,symbol,price,ts):

        self.db.execute(
        "INSERT INTO ticks VALUES (?,?,?)",
        (ts,symbol,price)
        )

        self.db.commit()

    def insert_candle(self,row):

        self.db.execute(
        "INSERT INTO candles VALUES (?,?,?,?,?,?,?)",
        row
        )

        self.db.commit()

    def get_last_prices(self,symbol,limit=20):

        cur = self.db.cursor()

        rows = cur.execute(
        "SELECT price FROM ticks WHERE symbol=? ORDER BY ts DESC LIMIT ?",
        (symbol,limit)
        ).fetchall()

        return [r[0] for r in rows]
