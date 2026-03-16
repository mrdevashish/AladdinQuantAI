import random
import time

class MarketEngine:

    def __init__(self):

        self.price = 23000
        self.gamma = "LOW"
        self.liquidity = "NONE"

    def update_price(self):

        move = random.randint(-50,50)
        self.price += move

    def gamma_engine(self):

        self.gamma = random.choice(["HIGH","LOW"])

    def liquidity_engine(self):

        self.liquidity = random.choice(["BUY","SELL"])

    def run(self):

        while True:

            self.update_price()
            self.gamma_engine()
            self.liquidity_engine()

            time.sleep(2)
