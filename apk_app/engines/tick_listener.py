import subprocess
import ast
import time

from database.db_router import DBRouter

db = DBRouter()

def run_listener():

    p = subprocess.Popen(
        ["python","fyers_wrapper/stream/live_feed.py"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in p.stdout:

        line=line.strip()

        if line.startswith("{"):

            try:

                msg = ast.literal_eval(line)

                if "symbol" in msg and "ltp" in msg:

                    symbol = msg["symbol"]
                    price = msg["ltp"]
                    ts = int(time.time())

                    db.insert_tick(symbol,price,ts)

            except:
                pass
