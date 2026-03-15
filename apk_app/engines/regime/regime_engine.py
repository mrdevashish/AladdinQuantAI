from database.db_router import DBRouter
import numpy as np

db = DBRouter()

class RegimeEngine:

    def detect(self,symbol):

        prices = db.get_last_prices(symbol,50)

        if len(prices) < 20:
            return

        vol = np.std(prices)

        trend = prices[0] - prices[-1]

        if abs(trend) > 40:

            print("TREND MARKET",symbol)

        elif vol < 5:

            print("LOW VOLATILITY RANGE",symbol)

        elif vol > 30:

            print("HIGH VOLATILITY",symbol)

        else:

            print("RANGE MARKET",symbol)
