class HedgingPressure:

    def detect(self,chain):

        call_oi=0
        put_oi=0

        for row in chain:

            if row["optionType"]=="CE":
                call_oi += row["openInterest"]

            if row["optionType"]=="PE":
                put_oi += row["openInterest"]

        if call_oi > put_oi * 1.5:

            print("MARKET MAKERS HEDGING UPSIDE")

        if put_oi > call_oi * 1.5:

            print("MARKET MAKERS HEDGING DOWNSIDE")
