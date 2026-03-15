from database.db_router import DBRouter

db = DBRouter()

class SpoofingDetector:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 20)

        if len(prices) < 10:
            return

        spike = max(prices) - min(prices)

        if spike > 80:

            print("POSSIBLE SPOOFING MOVE", symbol)
