from school import School
from person import Student,Teacher
from subject import Subject
from classroom import Classroom

school = School("abc","dhaka")


#adding classroom
eight = Classroom("eight")
nine = Classroom("nine")
ten = Classroom("ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


#adding student
rahim = Student("Rahim",eight)
karim = Student("Karim",nine)
fahim = Student("Fahim",ten)
hamim = Student("Hamim",ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)


#adding teachers
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Khan")

#adding subjects
bangla = Subject('Bangla',abul)
physics = Subject('Physics',babul)
chemistry = Subject('Chemistry',kabul)
biology = Subject('Biology',kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
# eight.add_subject(biology)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)

eight.take_semester_final_exam()
# nine.take_semester_final_exam()
# ten.take_semester_final_exam()

print(school)



