def checkInclusion(self, s1: str, s2: str) -> bool:
    
    s1Counter = Counter(s1)
    s2Counter = Counter(s2[:len(s1)-1])
    
    for i in range(len(s1)-1, len(s2)):
        current,start = i, i-len(s1)+1
        s2Counter[s2[current]] += 1
        
        if s2Counter == s1Counter:
            return True
        
        s2Counter[s2[start]] -= 1
        
        if s2Counter[s2[start]] == 0:
            del s2Counter[s2[start]]
            
    return False
