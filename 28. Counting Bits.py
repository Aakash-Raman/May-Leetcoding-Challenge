class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i>>1] + int(i & 1))
        return res
