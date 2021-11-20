class Grade:
    def __init__(self,id,subject_name,student_id,grade):
        self.id = id
        self.subject_name = subject_name
        self.student_id = student_id
        self.grade = grade

    def __repr__(self):
        return f'The grade data is: (the id = {self.id}, the student name is: {self.subject_name}),' \
               f'the student id is: ({self.student_id} and the student grade is: {self.grade})'

    def __str__(self):
        return f'The grade data is: the id = {self.id}, the student name is: {self.subject_name},' \
               f'the student id is: {self.student_id} and the student grade is: {self.grade}'

    def __eq__(self, other):
        if isinstance(other,Grade):
            return self.grade == other.grade
        elif type(other) in [int]:
            return self.id == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other,Grade):
            return self.grade > other.grade
        elif type(other) in [int]:
            return self.id > other
        else:
            return False

    def __lt__(self, other):
        if isinstance(other,Grade):
            return self.grade < other.grade
        elif type(other) in [int]:
            return self.id < other
        else:
            return False

    def __add__(self):
        self.grade += other
        return self
    
    def __sub__(self, other):
        self.grade -= other
        return self
