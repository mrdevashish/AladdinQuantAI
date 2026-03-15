import random

class OptionsAI:

    def fetch_options_chain(self):

        data=[]

        for strike in range(23000,23300,50):

            row={
                "strike":strike,
                "gamma":random.uniform(0,1),
                "oi":random.randint(1000,5000)
            }

            data.append(row)

        return data
