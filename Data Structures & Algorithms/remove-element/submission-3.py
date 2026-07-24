class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ctr = 0

        length = len(nums)

        for num in range(len(nums)):
            if num == val:
                ctr += 1
        return length -ctr