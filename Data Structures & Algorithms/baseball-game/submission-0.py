class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for n in range(len(operations)):
            if operations[n] == "+":
                score.append(score[-1] + score[-2])
            elif operations[n] == "D":
                score.append(2 * score[-1])
            elif operations[n] == "C":
                score.pop()
            else:
                score.append(int(operations[n]))

        return sum(score)

        