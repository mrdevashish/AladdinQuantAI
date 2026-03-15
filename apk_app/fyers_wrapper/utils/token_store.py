import json
import os

TOKEN_FILE="fyers_wrapper/config/access_token.json"

def save_token(token):
    with open(TOKEN_FILE,"w") as f:
        json.dump({"access_token":token},f)

def load_token():
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE) as f:
        return json.load(f)["access_token"]
