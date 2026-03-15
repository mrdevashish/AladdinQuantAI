from fyers_apiv3 import fyersModel
from fyers_wrapper.utils.token_store import load_token
import json

with open("fyers_wrapper/config/config.json") as f:
    cfg=json.load(f)

client_id=cfg["client_id"]
token=load_token()

fyers=fyersModel.FyersModel(client_id=client_id,token=token)

class OptionsAI:

    def fetch(self):

        data={
        "symbol":"NSE:NIFTY50-INDEX",
        "strikecount":20,
        "timestamp":""
        }

        res=fyers.optionchain(data)

        return res["data"]["optionsChain"]
