from engines.event_bus import get_event

class AIStrategy:

    def run(self):

        event = get_event()

        if not event:
            return

        symbol = event["symbol"]
        price = event["price"]

        if int(price) % 100 == 0:

            print("AI SIGNAL BUY",symbol)
