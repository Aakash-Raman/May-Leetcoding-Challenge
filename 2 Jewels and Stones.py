class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ctr = 0
        for i in J:
            for j in S:
                if(j == i):
                    ctr += 1
        return ctr
