class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for n in range(len(arr)-2, -1, -1):
            if arr[n] <= k:
                arr[n] = k
            else:
                a = arr[n]
                arr[n] = k
                k = a
        return arr

            
            

        