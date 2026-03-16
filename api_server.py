import json
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# ----------------------------------
# IMPORT YOUR EXISTING ENGINES
# ----------------------------------

from engines.gamma.gamma_trap import GammaTrapEngine
from engines.liquidity.liquidity_engine import LiquidityEngine
from engines.strategy.ai_strategy import AIStrategy


# ----------------------------------
# GLOBAL STATE
# ----------------------------------

market_state = {
    "price": 0,
    "gamma": "NONE",
    "liquidity": "NONE",
    "signal": "HOLD"
}


# ----------------------------------
# AI PIPELINE
# ----------------------------------

class TradingPipeline:

    def __init__(self):

        self.gamma_engine = GammaTrapEngine()
        self.liquidity_engine = LiquidityEngine()
        self.strategy_engine = AIStrategy()

    def run(self):

        while True:

            try:

                gamma = self.gamma_engine.detect()
                liquidity = self.liquidity_engine.detect()

                signal = self.strategy_engine.generate(
                    gamma,
                    liquidity
                )

                market_state["gamma"] = gamma
                market_state["liquidity"] = liquidity
                market_state["signal"] = signal

                time.sleep(2)

            except Exception as e:

                print("Engine error:", e)
                time.sleep(5)


# ----------------------------------
# API SERVER
# ----------------------------------

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/signals":

            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(market_state).encode()
            )


# ----------------------------------
# START SERVER
# ----------------------------------

def run_server():

    server = HTTPServer(("0.0.0.0",9001), Handler)
    print("AI trading server running on port 9001")
    server.serve_forever()


def start_pipeline():

    pipeline = TradingPipeline()
    pipeline.run()


if __name__ == "__main__":

    thread = threading.Thread(target=start_pipeline)
    thread.daemon = True
    thread.start()

    run_server()
