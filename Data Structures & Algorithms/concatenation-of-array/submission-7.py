class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        ans = nums + ans

        return ans