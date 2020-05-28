class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dict = {}
        sub = 0
        ctr = 0
        for i in range(0,len(nums)):
            if(nums[i]==1):
                ctr += 1
            else:
                ctr -= 1
            if(ctr == 0):
                sub = i+1
            if(ctr in dict):
                sub = max(sub,i-dict[ctr])
            else:
                dict[ctr] = i
        return sub    
    
