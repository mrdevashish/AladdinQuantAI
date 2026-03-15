class GammaTrap:

    def detect(self,chain):

        call_gamma=0
        put_gamma=0

        for row in chain:

            gamma=row.get("gamma",0)

            if row["optionType"]=="CE":
                call_gamma += gamma

            if row["optionType"]=="PE":
                put_gamma += gamma

        if abs(call_gamma-put_gamma) < 0.1:

            print("GAMMA TRAP DETECTED")
