from database.db_router import DBRouter
import numpy as np

db = DBRouter()

class BidAskImbalance:

    def detect(self, symbol):

        prices = db.get_last_prices(symbol, 30)

        if len(prices) < 10:
            return

        prices = np.array(prices)

        up_moves = np.sum(np.diff(prices) > 0)
        down_moves = np.sum(np.diff(prices) < 0)

        if up_moves > down_moves * 2:
            print("BID DOMINANCE", symbol)

        if down_moves > up_moves * 2:
            print("ASK DOMINANCE", symbol)
