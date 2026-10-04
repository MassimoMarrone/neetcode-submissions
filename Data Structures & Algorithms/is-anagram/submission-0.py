class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1, freq2 = {},{}
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            first = freq1.get(s[i],0)
            if(t[i] not in freq2):
                freq2[t[i]] = 0
            freq1[s[i]] = freq1.get(s[i],0) + 1
            freq2[t[i]] = freq2.get(t[i],0) + 1
        if freq1 == freq2:
            return True
        return False
        
        