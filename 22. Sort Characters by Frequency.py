def frequencySort(self, s: str) -> str:
        ans = ''
        for c, freq in collections.Counter(s).most_common():
            ans += c*freq
        return ans
