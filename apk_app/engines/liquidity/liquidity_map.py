from database.db_router import DBRouter
import numpy as np

db = DBRouter()

class LiquidityMap:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 100)

        if len(prices) < 30:
            return

        prices = np.array(prices)

        # detect clusters (levels where price repeated)
        unique, counts = np.unique(prices.round(1), return_counts=True)

        clusters = unique[counts > 3]

        if len(clusters) > 0:

            print("STOP LOSS CLUSTERS:", symbol)

            for c in clusters[:5]:
                print("  level:", c)
