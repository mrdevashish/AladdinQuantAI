from fyers_apiv3.FyersWebsocket.data_ws import FyersDataSocket
from config.fyers_config import CLIENT_ID, ACCESS_TOKEN, SYMBOL

token = CLIENT_ID + ":" + ACCESS_TOKEN

def onmessage(message):
    print("LIVE DATA:", message)

def onerror(message):
    print("ERROR:", message)

def onclose(message):
    print("Closed:", message)

def onopen():
    data_type = "SymbolUpdate"

    symbols = [SYMBOL]

    fyers.subscribe(symbols=symbols, data_type=data_type)
    fyers.keep_running()

fyers = FyersDataSocket(
    access_token=token,
    log_path="",
    litemode=False,
    write_to_file=False,
    reconnect=True,
    on_connect=onopen,
    on_close=onclose,
    on_error=onerror,
    on_message=onmessage
)

fyers.connect()
