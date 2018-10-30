from Student import Student


class CSstudent(Student):

    def __init__(self, first_name, last_name, major, gpa, is_on_probation):
        Student.__init__(self, first_name, last_name,
                         major, gpa, is_on_probation)

    def write_program(self):
        print(f"Yea {self.first_name} is a {self.major} student and can write programs")
