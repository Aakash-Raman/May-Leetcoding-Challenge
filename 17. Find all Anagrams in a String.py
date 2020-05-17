class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen = len(s)
        plen = len(p)
        if(slen < plen):
            return []
        
        p_count = Counter(p)
        s_count = Counter()
        
        result = []
        for i in range(slen):
            s_count[s[i]] += 1
            if(i >= plen):
                if(s_count[s[i - plen]] == 1):
                    del s_count[s[i - plen]]
                else:
                    s_count[s[i - plen]] -= 1
            if(p_count == s_count):
                result.append(i - plen + 1)
        return result
