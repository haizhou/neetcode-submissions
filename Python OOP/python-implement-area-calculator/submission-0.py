import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, arg1: int, arg2: int = 0) -> int:
        self.arg1 = arg1
        self.arg2 = arg2
        if self.arg2 == 0:
            return round(math.pi * arg1 ** 2, 2)
        else:
            return round(arg1 * arg2, 2)

    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
