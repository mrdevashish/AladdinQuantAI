from database.db_router import DBRouter

db=DBRouter()

class PatternSearch:

    def search(self,symbol):

        prices=db.get_last_prices(symbol,50)

        if len(prices)<30:
            return

        last_move=prices[0]-prices[10]

        if abs(last_move)>60:

            print("PATTERN MATCH: STRONG MOMENTUM")
