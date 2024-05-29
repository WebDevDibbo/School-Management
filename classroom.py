class Classroom:
    def __init__(self,name) -> None:
        self.name = name
        self.students = []
        self.subjects = []
        #* subjects is a list of object (where key is subject.name) and (value is an object of teacher subject.teacher.name)

    def add_student(self,student):
        roll_no = f"{self.name}-{len(self.students)+1}"
        student.id = roll_no
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
#* student.name-->Rahim student.classroom.name-->eight -->student.marks{'Bangla': 89, 'Physics': 41, 'Chemistry': 65, 'Biology': 26}
            # print(f"student-->{student.name},{student.classroom.name},{student.marks}\n")
            # print(f"studentinfo---->{student.id},{student.subject_grade},{student.grade},{len(self.students)}\n")
            # print(student[student.name])
            student.calculate_final_grade()