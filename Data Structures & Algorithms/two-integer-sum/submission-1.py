class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i,j in enumerate(nums):
            if target - j in n:
                return [n[target - j],i]
            n[j] = i
        return [1]