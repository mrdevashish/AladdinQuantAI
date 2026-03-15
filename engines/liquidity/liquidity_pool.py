from database.db_router import DBRouter

db = DBRouter()

class LiquidityPool:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 50)

        if len(prices) < 20:
            return

        high = max(prices)
        low = min(prices)

        last = prices[0]

        if abs(last - high) < 5:

            print("LIQUIDITY POOL ABOVE", symbol, high)

        if abs(last - low) < 5:

            print("LIQUIDITY POOL BELOW", symbol, low)
