class Solution:
    def isValid(self, s: str) -> bool:
        answerchar = {'}':'{', ']':'[', ')':'('}
        satck = []
        for i in s:
            if i in answerchar:
                if satck and satck[-1] == answerchar[i]:
                    satck.pop()
                else:
                    return False
            else:
                satck.append(i)
        
        return len(satck) == 0

            



        