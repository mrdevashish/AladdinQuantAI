import json
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# ------------------------------
# AI ENGINE
# ------------------------------

class AIEngine:

    def __init__(self):
        self.price = 0
        self.gamma = "LOW"
        self.liquidity = "NONE"
        self.signal = "HOLD"

    def update_market(self):
        self.price = random.randint(23000,24000)

    def gamma_engine(self):
        self.gamma = random.choice(["HIGH","LOW"])

    def liquidity_engine(self):
        self.liquidity = random.choice(["BUY","SELL"])

    def signal_engine(self):

        if self.gamma == "HIGH" and self.liquidity == "BUY":
            self.signal = "BUY"

        elif self.gamma == "HIGH" and self.liquidity == "SELL":
            self.signal = "SELL"

        else:
            self.signal = "HOLD"

    def run(self):

        while True:

            self.update_market()
            self.gamma_engine()
            self.liquidity_engine()
            self.signal_engine()


engine = AIEngine()

thread = threading.Thread(target=engine.run)
thread.daemon = True
thread.start()


# ------------------------------
# API SERVER
# ------------------------------

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/signals":

            data = {

                "price": engine.price,
                "gamma": engine.gamma,
                "liquidity": engine.liquidity,
                "signal": engine.signal

            }

            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())


def run():

    server = HTTPServer(("0.0.0.0",8000),Handler)
    print("AI trading server running")
    server.serve_forever()


if __name__ == "__main__":
    run()
