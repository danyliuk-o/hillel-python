class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record book: {self.record_book}"


class GroupLimitError(Exception):

    def __init__(self, limit):
        super().__init__(f'Група не може містити більше {limit} студентів')
        self.limit = limit


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise GroupLimitError(self.MAX_STUDENTS)
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'


gr = Group('PD1')
for i in range(1, 11):
    gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'AN{i}'))
assert len(gr.group) == 10, 'Test1'

try:
    gr.add_student(Student('Female', 25, 'Liza', 'Taylor', 'AN145'))  # 11 студент
except GroupLimitError as e:
    print(e)
assert len(gr.group) == 10, 'Test2'
assert gr.find_student('Taylor') is None, 'Test3'

gr.delete_student('Surname1')
gr.add_student(Student('Female', 25, 'Liza', 'Taylor', 'AN145'))  # місце звільнилось
assert len(gr.group) == 10, 'Test4'
