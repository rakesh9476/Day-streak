class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for candidate in set(nums):
            if nums.count(candidate) > n // 2:
                return candidate
