class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and (sandwiches[0] in students):
            for n in students:
                if n == sandwiches[0]:
                    sandwiches.pop(0)
                    students.remove(n)
        return len(sandwiches)


            
        