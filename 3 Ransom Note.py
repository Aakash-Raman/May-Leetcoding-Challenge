class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote) > len(magazine)):
            return False
        
        dict = {}
        for i in magazine:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for i in ransomNote:
            if(i not in dict):
                return False
            if(dict[i] <= 0):
                return False
            dict[i] -= 1
            
        return True
