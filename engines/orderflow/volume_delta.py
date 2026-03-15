from database.db_router import DBRouter

db = DBRouter()

class VolumeDelta:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 20)

        if len(prices) < 10:
            return

        delta = prices[0] - prices[-1]

        if delta > 30:
            print("BUYING DELTA", symbol)

        if delta < -30:
            print("SELLING DELTA", symbol)
