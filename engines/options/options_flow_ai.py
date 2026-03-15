from fyers_apiv3 import fyersModel
from fyers_wrapper.utils.token_store import load_token
import json

with open("fyers_wrapper/config/config.json") as f:
    cfg=json.load(f)

client_id=cfg["client_id"]
token=load_token()

fyers=fyersModel.FyersModel(client_id=client_id,token=token)


class OptionsFlowAI:

    def fetch_chain(self):

        data={
            "symbol":"NSE:NIFTY50-INDEX",
            "strikecount":20,
            "timestamp":""
        }

        res=fyers.optionchain(data)

        if "data" not in res:
            return []

        return res["data"].get("optionsChain",[])


    def unusual_activity(self,chain):

        for row in chain:

            strike=row.get("strikePrice") or row.get("strike_price") or row.get("strike")
            opt=row.get("optionType") or row.get("option_type")

            oi=row.get("openInterest",0)
            vol=row.get("volume",0)

            if oi and vol and vol>oi*0.5:

                print("UNUSUAL OPTIONS ACTIVITY",strike,opt)


    def dealer_hedging(self,chain):

        call_oi=0
        put_oi=0

        for row in chain:

            oi=row.get("openInterest",0)

            opt=row.get("optionType") or row.get("option_type")

            if opt=="CE":
                call_oi+=oi

            if opt=="PE":
                put_oi+=oi

        if call_oi>put_oi*1.5:

            print("DEALERS HEDGING UPSIDE")

        if put_oi>call_oi*1.5:

            print("DEALERS HEDGING DOWNSIDE")


    def gamma_walls(self,chain):

        levels={}

        for row in chain:

            strike=row.get("strikePrice") or row.get("strike")

            gamma=row.get("gamma",0)

            oi=row.get("openInterest",0)

            exposure=gamma*oi

            if strike:

                levels[strike]=levels.get(strike,0)+exposure

        strong=sorted(levels.items(),key=lambda x:x[1],reverse=True)[:3]

        for s in strong:

            print("GAMMA WALL",s[0])


    def max_pain(self,chain):

        strikes={}

        for row in chain:

            strike=row.get("strikePrice") or row.get("strike")

            oi=row.get("openInterest",0)

            if strike:

                strikes[strike]=strikes.get(strike,0)+oi

        if not strikes:
            return

        maxpain=max(strikes,key=strikes.get)

        print("MAX PAIN LEVEL",maxpain)


    def run(self):

        chain=self.fetch_chain()

        if not chain:
            return

        self.unusual_activity(chain)

        self.dealer_hedging(chain)

        self.gamma_walls(chain)

        self.max_pain(chain)
