from fyers_apiv3 import fyersModel
from config.fyers_config import CLIENT_ID, ACCESS_TOKEN

fyers = fyersModel.FyersModel(
    client_id=CLIENT_ID,
    token=ACCESS_TOKEN
)

data = {
    "symbol": "NSE:NIFTY50-INDEX",
    "resolution": "5",
    "date_format": "1",
    "range_from": "2025-01-01",
    "range_to": "2025-02-01",
    "cont_flag": "1"
}

response = fyers.history(data=data)

print(response)
