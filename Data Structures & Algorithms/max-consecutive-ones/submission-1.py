class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ctr = 0
        max_ctr = 0

        for num in nums:
            if num == 1:
                ctr += 1
                max_ctr = max(max_ctr, ctr)
            else:
                ctr = 0

        return max_ctr