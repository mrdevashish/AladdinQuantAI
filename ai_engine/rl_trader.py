import random

class RLTrader:

    def decide(self,price):

        action = random.choice(["BUY","SELL","HOLD"])

        print("RL Decision:",action,"price",price)
