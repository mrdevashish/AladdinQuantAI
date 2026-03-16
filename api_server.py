import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from market_engine import MarketEngine
from strategy_engine import StrategyEngine
from backtest_engine import BacktestEngine

market = MarketEngine()
strategy = StrategyEngine()
backtest = BacktestEngine()

state = {
    "price":0,
    "gamma":"LOW",
    "liquidity":"NONE",
    "signal":"HOLD"
}


def market_loop():

    while True:

        market.update_price()
        market.gamma_engine()
        market.liquidity_engine()

        state["price"] = market.price
        state["gamma"] = market.gamma
        state["liquidity"] = market.liquidity

        state["signal"] = strategy.generate_signal(
            market.gamma,
            market.liquidity
        )


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/signals":

            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            self.wfile.write(json.dumps(state).encode())

        elif self.path == "/backtest":

            result = backtest.run_backtest()

            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            self.wfile.write(json.dumps(result).encode())


def run():

    thread = threading.Thread(target=market_loop)
    thread.daemon = True
    thread.start()

    server = HTTPServer(("0.0.0.0",9500),Handler)

    print("AI trading server running on port 9500")

    server.serve_forever()


if __name__ == "__main__":
    run()
