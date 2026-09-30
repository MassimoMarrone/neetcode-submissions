# Given a string of length n made of 'W' and 'B' characters and an integer k (1 <= k <= n),
# find the minimum number of 'W' -> 'B' recolorings needed so that the string
# contains a substring of length k made only of 'B'.
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        count = 0
        for a in range(k):
            if blocks[a] == "W":
                count +=1
        best = count
        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                count += 1 
            if blocks[l] == "W":
                count -=1
            l += 1
            best = min(best, count)
        return best
