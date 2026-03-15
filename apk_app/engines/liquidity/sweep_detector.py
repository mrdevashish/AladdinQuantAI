from database.db_router import DBRouter

db=DBRouter()

class LiquiditySweep:

    def detect(self,symbol):

        prices=db.get_last_prices(symbol,15)

        if len(prices)<10:
            return

        move=prices[0]-prices[-1]

        if abs(move)>80:

            print("STOP HUNT / LIQUIDITY SWEEP",symbol)
