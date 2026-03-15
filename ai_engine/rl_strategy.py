import random

class RLStrategy:

    def decide(self,price):

        actions=["BUY","SELL","HOLD"]

        action=random.choice(actions)

        print("RL STRATEGY DECISION",action,"price",price)
