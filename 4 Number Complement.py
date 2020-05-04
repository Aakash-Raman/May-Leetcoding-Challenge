class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        bit = 1
        while(num > 0):
            temp = temp ^ bit
            bit = bit << 1
            num = num >> 1
        return temp
