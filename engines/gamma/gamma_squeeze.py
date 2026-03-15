class GammaSqueeze:

    def detect(self,chain):

        exposure=0

        for row in chain:

            gamma=row.get("gamma",0)
            oi=row.get("openInterest",0)

            exposure += gamma * oi

        if exposure > 100000:

            print("⚠ GAMMA SQUEEZE POSSIBLE")
