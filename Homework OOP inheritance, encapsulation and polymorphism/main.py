class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self):
        grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades) / len(grades) if grades else 0
        
    def __str__(self):
        avg = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return  (f"Имя: {self.name}\n"
                 f"Фамилия: {self.surname}\n"
                 f"Средняя оценка за домашние задания: {round(avg + 0.01, 1)}\n"
                 f"Курсы в процессе изучения: {courses_in_progress}\n"
                 f"Завершенные курсы: {finished_courses}")
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented
    

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(grades) / len(grades) if grades else 0    

    def __str__(self):
        avg = self.average_grade()
        return  (f"Имя: {self.name}\n"
                 f"Фамилия: {self.surname}\n"
                 f"Средняя оценка за лекции: {round(avg + 0.01, 1)}")
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return  (f"Имя: {self.name}\n"
                 f"Фамилия: {self.surname}")
        

def avg_st_by_course(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def avg_lec_by_course(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Входные данные для проверки 

student1 = Student('Mike', 'S.', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Milly', 'K.', 'female')
student2.courses_in_progress += ['Python', 'OOP']
student2.finished_courses += ['Основы программирования']

lecturer1 = Lecturer('John', 'L.')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Jane', 'P.')
lecturer2.courses_attached += ['Python', 'OOP']

reviewer1 = Reviewer('Hale', 'R.')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Jully', 'I.')
reviewer2.courses_attached += ['Python', 'OOP']

reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 7)

reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'OOP', 10)

student1.rate_lecturer(lecturer1, 'Python', 6)
student1.rate_lecturer(lecturer1, 'Python', 7)
student1.rate_lecturer(lecturer1, 'Git', 7)

student2.rate_lecturer(lecturer2, 'Python', 6)
student2.rate_lecturer(lecturer2, 'Python', 7)
student2.rate_lecturer(lecturer2, 'OOP', 9)

print("\nСтудент 1:")
print(student1)

print("\nСтудент 2:")
print(student2)

print("\nЛектор 1:")
print(lecturer1)

print("\nЛектор 2:")
print(lecturer2)

print("\nПроверяющий 1:")
print(reviewer1)

print("\nПроверяющий 2:")
print(reviewer2)

print("\nСравнение студентов:")
print(f"{student1.name} {student1.surname} < {student2.name} {student2.surname}: {student1 < student2}")
print(f"{student1.name} {student1.surname} <= {student2.name} {student2.surname}: {student1 <= student2}")
print(f"{student1.name} {student1.surname} == {student2.name} {student2.surname}: {student1 == student2}")

print("\nСравнение лекторов:")
print(f"{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname}: {lecturer1 < lecturer2}")
print(f"{lecturer1.name} {lecturer1.surname} <= {lecturer2.name} {lecturer2.surname}: {lecturer1 <= lecturer2}")
print(f"{lecturer1.name} {lecturer1.surname} == {lecturer2.name} {lecturer2.surname}: {lecturer1 == lecturer2}")

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("\nСредняя оценка за домашние задания по курсам:")
print(f"{avg_st_by_course(students, 'Python')} - курс Python")
print(f"{avg_st_by_course(students, 'Git')} - курс Git")
print(f"{avg_st_by_course(students, 'OOP')} - курс OOP")

print("\nСредняя оценка за лекции по курсам:")
print(f"{avg_lec_by_course(lecturers, 'Python')} - курс 'Python'")
print(f"{avg_lec_by_course(lecturers, 'Git')} - курс 'Git'")
print(f"{avg_lec_by_course(lecturers, 'OOP')} - курс 'OOP'")