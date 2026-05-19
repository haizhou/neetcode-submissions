class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations :
            if i == '+' and len(stack)>=2:
                stack.append(stack[-1]+stack[-2])
            elif i == 'D' and stack:
                stack.append(2*stack[-1])
            elif i == 'C' and stack:
                del stack[-1]
            else:
                stack.append(int(i))
        return sum(stack)
