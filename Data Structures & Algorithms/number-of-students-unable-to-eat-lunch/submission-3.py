class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        lunch_line = deque(students)
        i = 0
        while lunch_line:
            if count == len(lunch_line):
                break
            student = lunch_line.popleft()
            if student == sandwiches[i]:
                i += 1
                count = 0
            else:
                lunch_line.append(student)
                count += 1
        return len(lunch_line)

            
        