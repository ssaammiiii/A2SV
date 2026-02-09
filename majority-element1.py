from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = 1 + n//2
        freq = Counter(nums)
        for key in freq:
            if freq[key] >= majority:
                return key 
