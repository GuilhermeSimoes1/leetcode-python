class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        dire = []
        radiant = []

        for i in range(len(senate)):

            if senate[i] == "D":
                dire.append(i)
            else:
                radiant.append(i)

        while dire and radiant:

            lenght = len(senate)

            r = radiant.pop(0)
            d = dire.pop(0)

            if r < d:
                radiant.append(r + lenght)
            else:
                dire.append(d + lenght)

        if dire:
            return "Dire"
        else:
            return "Radiant"




