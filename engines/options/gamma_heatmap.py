class GammaHeatmap:

    def build(self,chain):

        heatmap={}

        for row in chain:

            strike=row.get("strikePrice") or row.get("strike")

            gamma=row.get("gamma",0)

            oi=row.get("openInterest",0)

            exposure=gamma*oi

            if strike:

                heatmap[strike]=heatmap.get(strike,0)+exposure

        top=sorted(heatmap.items(),key=lambda x:x[1],reverse=True)[:5]

        for t in top:

            print("GAMMA EXPOSURE LEVEL",t[0],t[1])
