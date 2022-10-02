
class Student:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.aver_rating = float()

    def __str__(self) -> str:
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for grade in self.grades:
            del self.grades[grade][0]
            grades_count += len(self.grades[grade])
        
        self.aver_rating = sum(map(sum, self.grades.values())) / grades_count
        
        result = f'Фамилия: {self.last_name}\n' \
                 f'Имя: {self.first_name}\n' \
                 f'Отчество: {self.middle_name}\n' \
                 f'Средняя оценка за ДЗ: {self.aver_rating:.2f}\n' \
                 f'Текущие курсы: {courses_in_progress_string}\n' \
                 f'Завершенные кусры: {finished_courses_string}\n'

        return result

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неверное сравнение')
            return
        return self.aver_rating < other.aver_rating
        
class Mentor:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, first_name, middle_name, last_name):
        super().__init__(first_name, middle_name, last_name)
        self.aver_rating = float()
        self.grades = {}

    def __str__(self) -> str:
        grades_count = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
        
        try:
            self.aver_rating = sum(map(sum, self.grades.values())) / grades_count
        except ZeroDivisionError:
            grades_count = 0

        result = f'Фамилия: {self.last_name}\n' \
                 f'Имя: {self.first_name}\n' \
                 f'Отчество: {self.middle_name}\n' \
                 f'Средняя оценка по лекциям: {self.aver_rating:.2f}\n'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Неверное сравнение')
            return
        return self.aver_rating < other.aver_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [course]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        result = f'Фамилия: {self.last_name}\n' \
                 f'Имя: {self.first_name}\n' \
                 f'Отчество: {self.middle_name}\n'
        return result
    
 
# Создаем лекторов и закрепляем их за курсом
lecturer_1 = Lecturer('Анна', 'Владимировна', 'Большакова')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Вадим', 'Германович', 'Пак')
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Антон', 'Львович', 'Иванов')
lecturer_3.courses_attached += ['Python']

# Создаем проверяющих и закрепляем их за курсом
reviewer_1 = Reviewer('Мария', 'Николаевна', 'Парашют')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Артем', 'Павлович', 'Болтушкин')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Денис', 'Федорович', 'Астахов')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Java']

student_2 = Student('Дмитрий', 'Михайлович', 'Козырев')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Евгения', 'Вячеславовна', 'Антонова')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Java']

# Выставляем оценки лекторам за лекции
student_1.rate_hw(lecturer_1, 'Python', 1)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 7)

student_1.rate_hw(lecturer_2, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Python', 3)
student_1.rate_hw(lecturer_2, 'Python', 10)

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 8)

student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 6)
student_2.rate_hw(lecturer_2, 'Java', 6)

student_3.rate_hw(lecturer_3, 'Python', 8)
student_3.rate_hw(lecturer_3, 'Python', 10)
student_3.rate_hw(lecturer_3, 'Python', 10)

# Выставляем оценки студентам за домашние задания
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 10)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)

reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 9)
reviewer_2.rate_hw(student_3, 'Python', 5)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 8)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}\n\n')

print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}\n\n')

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.first_name} {student_1.last_name} < {student_2.first_name} {student_2.last_name} = {student_1 < student_2}')

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.first_name} {lecturer_1.last_name} < {lecturer_2.first_name} {lecturer_2.last_name} = {lecturer_1 > lecturer_2}')

students_list = [student_1, student_2, student_3]
lecturers_list = [lecturer_1, lecturer_2, lecturer_3]

def rating_students(students_list, course_name):
    sum = 0
    count = 0
    for student in students_list:
        if student.courses_in_progress == [course_name]:
            sum += student.aver_rating
            count += 1
    aver_all = sum / count

    return aver_all

def rating_lecturers(lecturers_list, course_name):
    sum = 0
    count = 0
    for lecturer in lecturers_list:
        if lecturer.courses_attached == [course_name]:
            sum += lecturer.aver_rating
            count += 1
    aver_rating = sum / count
    
    return aver_rating


print(f"Средняя оценка всех студентов по курсу {'Python'}: {rating_students(students_list, 'Python'):.2f}")
print(f"Средняя оценка всех лекторов по курсу {'Python'}: {rating_lecturers(lecturers_list, 'Python'):.2f}\n")