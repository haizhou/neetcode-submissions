class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        capicity = len(nums)
        ans = [0] * 2 * capicity
        for n in range(len(ans)):
            if n <= capicity-1:
                ans[n] = nums[n]
            else:
                ans[n] = nums[n - capicity]
        return ans
        