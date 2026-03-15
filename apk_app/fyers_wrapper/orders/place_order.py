import json
from fyers_apiv3 import fyersModel
from fyers_wrapper.utils.token_store import load_token

with open("fyers_wrapper/config/config.json") as f:
    cfg=json.load(f)

client_id=cfg["client_id"]
token=load_token()

fyers=fyersModel.FyersModel(
    client_id=client_id,
    token=token
)

def buy(symbol="NSE:SBIN-EQ",qty=1):

    data={
        "symbol":symbol,
        "qty":qty,
        "type":2,
        "side":1,
        "productType":"INTRADAY",
        "limitPrice":0,
        "stopPrice":0,
        "validity":"DAY"
    }

    print(fyers.place_order(data))
