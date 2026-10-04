class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for i in strs:
            s = [0 for z in range(26)]
            for j in i:
                s[ord(j) - ord('a')] += 1 
            a.setdefault(tuple(s),[]).append(i)
        result = []
        for k,v in a.items():
            result.append(list(v))
        return result 


            