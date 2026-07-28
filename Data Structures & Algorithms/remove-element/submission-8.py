class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)

        for num in nums:
            if num == val:
                k -= 1
        
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return k
