class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, t1: str, t2: str = " ") -> str:
        self.t1 = t1
        self.t2 = t2
        if t2 == " ":
            return self.t1.upper()
        else:
            return self.t1 + self.t2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
