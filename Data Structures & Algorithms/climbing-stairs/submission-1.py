class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 :
            return n
        
        wayn_1 = 2
        wayn_2 = 1

        for i in range(3, n+1):
            wayn = wayn_1 + wayn_2
            wayn_2 = wayn_1
            wayn_1 = wayn
        
        return wayn
            




        

        