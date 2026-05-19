class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        target = -1
        for n in range(len(arr)-1, -1, -1):
            a = arr[n]
            arr[n] = target
            target = max(target, a)

        return arr

            
            

        