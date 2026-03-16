class StrategyEngine:

    def generate_signal(self, gamma, liquidity):

        if gamma == "HIGH" and liquidity == "BUY":
            return "BUY"

        if gamma == "HIGH" and liquidity == "SELL":
            return "SELL"

        return "HOLD"
