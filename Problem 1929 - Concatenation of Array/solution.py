class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)

        ans = [None] * (length * 2)

        for i in range(length):
            ans[i] = ans[i + length] = nums[i]
        return ans