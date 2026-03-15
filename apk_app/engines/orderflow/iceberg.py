from database.db_router import DBRouter

db = DBRouter()

class IcebergDetector:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 40)

        if len(prices) < 20:
            return

        level_hits = {}

        for p in prices:
            p = round(p,1)
            level_hits[p] = level_hits.get(p,0) + 1

        for level,count in level_hits.items():

            if count > 5:
                print("ICEBERG ORDER LEVEL", symbol, level)
