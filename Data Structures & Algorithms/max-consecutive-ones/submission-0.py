class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a, b , n = 0, 0, 0
        while n <= len(nums)-1:
            if nums[n] == 0:
                if a > b:
                    b = a
                a = 0
                n += 1
            else:
                a += 1
                n += 1
                if a > b:
                    b = a

        return b

                            

        