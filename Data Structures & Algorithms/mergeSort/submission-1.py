
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        s = 0 
        e = len(pairs) - 1
        
        m = (s + e) // 2

        left = pairs[:m+1]
        self.mergeSort(left)

        right = pairs[m+1:]
        self.mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1
            else:
                pairs[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1

        return pairs

        

