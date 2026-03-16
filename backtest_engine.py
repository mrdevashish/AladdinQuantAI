import random

class BacktestEngine:

    def run_backtest(self):

        balance = 100000
        trades = []

        for i in range(50):

            result = random.choice(["win","loss"])

            if result == "win":
                balance += 500

            else:
                balance -= 300

            trades.append(result)

        winrate = trades.count("win") / len(trades)

        return {
            "balance": balance,
            "winrate": round(winrate,2)
        }
