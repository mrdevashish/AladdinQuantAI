import duckdb

DB="database/market_memory.duckdb"

class PatternSearch:

    def find_similar(self,price):

        db = duckdb.connect(DB)

        rows = db.execute(
        "SELECT close FROM candles LIMIT 1000"
        ).fetchall()

        similar=[]

        for r in rows:

            p = r[0]

            if abs(p-price) < 10:

                similar.append(p)

        print("Found",len(similar),"similar price patterns")
