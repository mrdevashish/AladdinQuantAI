from database.tick_db import TickDB

class ReplayEngine:

    def run(self):

        db = TickDB()

        rows = db.db.execute(
            "SELECT symbol,price FROM ticks LIMIT 100"
        ).fetchall()

        for r in rows:

            symbol,price = r

            print("REPLAY",symbol,price)
