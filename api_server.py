import json
import random
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


# -------------------------------
# GLOBAL MARKET STATE
# -------------------------------

market_state = {
    "price": 0,
    "gamma": "NONE",
    "liquidity": "NONE",
    "signal": "HOLD"
}


# -------------------------------
# SIMPLE AI ENGINE LOOP
# -------------------------------

def ai_loop():

    while True:

        try:

            # temporary signals
            market_state["price"] = random.randint(23000,24000)

            market_state["gamma"] = random.choice(
                ["HIGH","LOW"]
            )

            market_state["liquidity"] = random.choice(
                ["BUY","SELL"]
            )

            if market_state["gamma"] == "HIGH" and market_state["liquidity"] == "BUY":
                market_state["signal"] = "BUY"

            elif market_state["gamma"] == "HIGH" and market_state["liquidity"] == "SELL":
                market_state["signal"] = "SELL"

            else:
                market_state["signal"] = "HOLD"

            time.sleep(2)

        except Exception as e:

            print("AI error:", e)
            time.sleep(5)


# -------------------------------
# API SERVER
# -------------------------------

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/signals":

            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(market_state).encode()
            )


# -------------------------------
# SERVER START
# -------------------------------

def run_server():

    server = HTTPServer(("0.0.0.0",9001), Handler)

    print("AI trading server running on port 9001")

    server.serve_forever()


if __name__ == "__main__":

    thread = threading.Thread(target=ai_loop)
    thread.daemon = True
    thread.start()

    run_server()
