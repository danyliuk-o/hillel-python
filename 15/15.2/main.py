from group import Group
from group_limit_error import GroupLimitError
from student import Student

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
assert st1 == Student('Male', 30, 'Steve', 'Jobs', 'AN142')
assert st1 != st2

gr.delete_student('Taylor')
print(gr)

gr = Group('PD2')
for i in range(1, 11):
    gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'AN{i}'))
try:
    gr.add_student(Student('Female', 25, 'Liza', 'Taylor', 'AN145'))
except GroupLimitError as e:
    print(e)
assert len(gr.group) == 10