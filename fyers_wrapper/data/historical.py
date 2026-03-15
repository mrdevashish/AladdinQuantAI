import json
from datetime import datetime,timedelta
from fyers_apiv3 import fyersModel
from fyers_wrapper.utils.token_store import load_token

with open("fyers_wrapper/config/config.json") as f:
    cfg=json.load(f)

client_id=cfg["client_id"]
token=load_token()

fyers=fyersModel.FyersModel(client_id=client_id,token=token)

def get_history(symbol="NSE:NIFTY50-INDEX"):

    end=datetime.today()
    start=end-timedelta(days=90)

    data={
        "symbol":symbol,
        "resolution":"5",
        "date_format":"1",
        "range_from":start.strftime("%Y-%m-%d"),
        "range_to":end.strftime("%Y-%m-%d"),
        "cont_flag":"1"
    }

    return fyers.history(data)

if __name__=="__main__":
    print(get_history())
