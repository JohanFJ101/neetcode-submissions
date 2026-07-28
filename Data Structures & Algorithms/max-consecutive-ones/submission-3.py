class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ctr = 0
        ctr = 0

        for num in nums:
            if num == 1:
                ctr += 1
            else:
                ctr=0
            if ctr > max_ctr:
                max_ctr = ctr

        return max_ctr