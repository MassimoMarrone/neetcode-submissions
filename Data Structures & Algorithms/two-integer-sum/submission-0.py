class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i,j in enumerate(nums):
            complement = target - j
            if complement in n:
                return [n[complement],i]
            n[j] = i
        return [1]