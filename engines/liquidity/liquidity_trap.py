from engines.event_bus import get_event

class LiquidityTrap:

    def __init__(self):
        self.prev = {}

    def run(self):

        event = get_event()

        if not event:
            return

        symbol = event["symbol"]
        price = event["price"]

        if symbol in self.prev:

            move = price - self.prev[symbol]

            if abs(move) > 20:

                print("LIQUIDITY SWEEP",symbol,move)

        self.prev[symbol] = price
