import json
from fyers_apiv3 import fyersModel
from fyers_wrapper.utils.token_store import load_token

with open("fyers_wrapper/config/config.json") as f:
    cfg=json.load(f)

client_id=cfg["client_id"]
token=load_token()

fyers=fyersModel.FyersModel(client_id=client_id,token=token)

def get_chain(symbol="NSE:NIFTY50-INDEX"):
    data={"symbol":symbol}
    return fyers.optionchain(data)

if __name__=="__main__":
    print(get_chain())
