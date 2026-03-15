from engines.event_bus import get_event

class OrderFlow:

    def __init__(self):
        self.history = []

    def run(self):

        event = get_event()

        if not event:
            return

        price = event["price"]

        self.history.append(price)

        if len(self.history) > 10:

            delta = price - self.history[-10]

            if delta > 50:
                print("SMART MONEY BUY PRESSURE")

            if delta < -50:
                print("SMART MONEY SELL PRESSURE")
