import json
from fyers_apiv3.FyersWebsocket import data_ws
from fyers_wrapper.utils.token_store import load_token

with open("fyers_wrapper/config/config.json") as f:
    cfg=json.load(f)

client_id=cfg["client_id"]
token=load_token()

access_token=f"{client_id}:{token}"

symbols=[
"NSE:NIFTY50-INDEX",
"NSE:NIFTYBANK-INDEX"
]

def onmessage(msg):
    print(msg)

def onerror(msg):
    print("error:",msg)

def onclose(msg):
    print("connection closed:",msg)

def onopen():
    ws.subscribe(symbols=symbols,data_type="symbolData")
    ws.keep_running()

ws=data_ws.FyersDataSocket(
    access_token=access_token,
    log_path="",
    litemode=False,
    write_to_file=False,
    reconnect=True,
    on_connect=onopen,
    on_close=onclose,
    on_error=onerror,
    on_message=onmessage
)

ws.connect()
