from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random


PORT = 8000


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/signals":

            data = {
                "price": random.randint(23000, 24000),
                "gamma": random.choice(["HIGH", "LOW"]),
                "liquidity": random.choice(["BUY", "SELL"])
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())


def run():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print("API server running on port", PORT)
    server.serve_forever()


if __name__ == "__main__":
    run()
