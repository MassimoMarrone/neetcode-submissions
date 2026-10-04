class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = {}
        for i in nums:
            top_k[i] = top_k.get(i,0) + 1

        ordinata = sorted(top_k, key = top_k.get,reverse = True)
        return ordinata[:k]


        