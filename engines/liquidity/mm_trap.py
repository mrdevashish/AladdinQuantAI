from database.db_router import DBRouter

db = DBRouter()

class MarketMakerTrap:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 20)

        if len(prices) < 10:
            return

        move = prices[0] - prices[-1]

        if abs(move) > 60:

            print("MARKET MAKER TRAP DETECTED", symbol)
