from engines.gamma.options_chain_fetch import fetch_options

class GammaEngine:

    def run(self):

        chain = fetch_options()

        exposure = 0

        for row in chain["data"]["optionsChain"]:

            gamma = row.get("gamma",0)
            oi = row.get("openInterest",0)

            exposure += gamma * oi

        if exposure > 100000:

            print("⚠ GAMMA SQUEEZE DETECTED")
