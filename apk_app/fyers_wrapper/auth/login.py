import json
from fyers_apiv3 import fyersModel
from fyers_wrapper.utils.token_store import save_token

with open("fyers_wrapper/config/config.json") as f:
    cfg = json.load(f)

client_id = cfg["client_id"]
secret_key = cfg["secret_key"]
redirect_uri = cfg["redirect_uri"]

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type="code",
    grant_type="authorization_code"
)

print("\nOPEN THIS URL IN BROWSER:\n")
print(session.generate_authcode())

auth_code = input("\nPaste auth code here:\n")

session.set_token(auth_code)

response = session.generate_token()

print("\nAPI RESPONSE:\n", response)

if response.get("s") != "ok":
    print("\nLogin failed")
    exit()

access_token = response["access_token"]

save_token(access_token)

print("\nACCESS TOKEN SAVED SUCCESSFULLY\n")
