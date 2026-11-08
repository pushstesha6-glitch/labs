import os

class Discipline:
    def __init__(self, name, department, specialties):
        self.name = name
        self.department = department
        self.specialties = specialties

    def is_for_specialty(self, specialty):
        return specialty in self.specialties


class Department:
    def __init__(self, name):
        self.name = name
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)
        discipline.department = self


class Student:
    def __init__(self, student_id, fio, specialty):
        self.student_id = student_id
        self.fio = fio
        self.specialty = specialty
        self.grades = {}
        self.semester = 1

    def enroll(self, discipline):
        if not discipline.is_for_specialty(self.specialty):
            raise ValueError(f"Дисциплины '{discipline.name}' нет для специальности '{self.specialty}'")
        if discipline in self.grades:
            raise ValueError(f"Вы уже записаны на '{discipline.name}'")
        self.grades[discipline] = None

    def unenroll(self, discipline):
        if discipline not in self.grades:
            raise ValueError(f"Вы не записаны на '{discipline.name}'")
        del self.grades[discipline]

    def set_grade(self, discipline, grade):
        if discipline not in self.grades:
            raise ValueError(f"Вы не записаны на '{discipline.name}'")
        if not (2 <= grade <= 5):
            raise ValueError("Оценка должна быть от 2 до 5")
        self.grades[discipline] = grade

    def promote(self):
        if not self.grades:
            raise ValueError("Студент не изучает ни одной дисциплины")
        for discipline, grade in self.grades.items():
            if grade is None:
                raise ValueError(f"Нет оценки по дисциплине '{discipline.name}'")
            if grade == 2:
                raise ValueError(f"Есть двойка по '{discipline.name}', перевод невозможен")

        self.semester += 1
        self.grades = {}
        return True

    def average_grade(self):
        valid_grades = [g for g in self.grades.values() if g is not None]
        if not valid_grades:
            return 0
        return sum(valid_grades) / len(valid_grades)


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []
        self.specialties = []

    def enroll_student(self, student_id, fio, specialty):
        if specialty not in self.specialties:
            raise ValueError(f"Специальности '{specialty}' нет на факультете")
        for s in self.students:
            if s.student_id == student_id:
                raise ValueError(f"Студент с ID {student_id} уже существует")

        new_student = Student(student_id, fio, specialty)
        self.students.append(new_student)
        return new_student

    def expel_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                return
        raise ValueError(f"Студента с ID {student_id} не найдено")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def find_discipline(self, name):
        for dep in self.departments:
            for d in dep.disciplines:
                if d.name.lower() == name.lower():
                    return d
        return None


def save_student_report(student):
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/student_{student.student_id}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Ведомость студента: {student.fio}\n")
        f.write(f"ID: {student.student_id}\n")
        f.write(f"Специальность: {student.specialty}\n")
        f.write(f"Семестр: {student.semester}\n")
        for discipline, grade in student.grades.items():
            dep_name = discipline.department.name if discipline.department else "—"
            grade_str = grade if grade is not None else "не выставлена"
            f.write(f"{discipline.name} (кафедра: {dep_name}) — {grade_str}\n")
        f.write(f"Средний балл: {student.average_grade():.2f}\n")
    return filename


def save_discipline_report(faculty, discipline):
    os.makedirs("reports", exist_ok=True)
    dep_name = discipline.department.name if discipline.department else "—"

    enrolled = []
    for s in faculty.students:
        if discipline in s.grades:
            enrolled.append((s, s.grades[discipline]))

    grades = [g for _, g in enrolled if g is not None]
    avg = sum(grades) / len(grades) if grades else 0

    filename = f"reports/discipline_{discipline.name}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Ведомость по дисциплине: {discipline.name}\n")
        f.write(f"Читающая кафедра: {dep_name}\n")
        f.write(f"Средний балл: {avg:.2f}\n")
        for s, g in enrolled:
            g_str = g if g is not None else "не выставлена"
            f.write(f"{s.student_id} {s.fio} — {g_str}\n")
    return filename


def build_demo_data():
    faculty = Faculty("РФиКТ")
    faculty.specialties = ["Прикладная информатика", "Кибербезопасность"]

    dep_is = Department("Кибербезопасности и информационных технологий")
    dep_ib = Department("Интеллектуальные и киберфизические системы")
    faculty.departments.extend([dep_is, dep_ib])

    d1 = Discipline("Базы данных", None, ["Прикладная информатика"])
    d2 = Discipline("Безопасность информационных систем", None, ["Кибербезопасность"])
    d3 = Discipline("Python", None, ["Прикладная информатика", "Кибербезопасность"])

    dep_is.add_discipline(d1)
    dep_ib.add_discipline(d2)
    dep_is.add_discipline(d3)

    faculty.enroll_student(101, "Иванов Иван", "Прикладная информатика")
    faculty.enroll_student(102, "Петров Петр", "Кибербезопасность")

    return faculty


def student_menu(faculty, student):
    while True:
        print(f"\n Студент: {student.fio} (ID {student.student_id}) | Семестр: {student.semester}")
        print("1. Записать на дисциплину")
        print("2. Убрать с дисциплины")
        print("3. Выставить оценку")
        print("4. Перевести в следующий семестр")
        print("5. Сохранить ведомость студента в файл")
        print("0. Назад в главное меню")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                name = input("Название дисциплины: ")
                d = faculty.find_discipline(name)
                if not d:
                    print("Такой дисциплины нет")
                    continue
                student.enroll(d)
                print("Записан")

            elif choice == "2":
                name = input("Название дисциплины: ")
                d = faculty.find_discipline(name)
                if not d:
                    print("Такой дисциплины нет")
                    continue
                student.unenroll(d)
                print("Удален с дисциплины")

            elif choice == "3":
                name = input("Название дисциплины: ")
                d = faculty.find_discipline(name)
                if not d:
                    print("Такой дисциплины нет")
                    continue
                grade = int(input("Оценка (2-5): "))
                student.set_grade(d, grade)
                print("Оценка выставлена")

            elif choice == "4":
                student.promote()
                print(f"Переведен на {student.semester} семестр")

            elif choice == "5":
                path = save_student_report(student)
                print(f"Ведомость сохранена: {path}")

            elif choice == "0":
                break
            else:
                print("Неверный ввод")

        except ValueError as e:
            print(f"Ошибка: {e}")


def main():
    faculty = build_demo_data()

    while True:
        print(f"\n Факультет: {faculty.name} ")
        print("1. Зачислить нового студента")
        print("2. Отчислить студента")
        print("3. Выбрать студента")
        print("4. Ведомость по дисциплине")
        print("0. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                sid = int(input("Введите ID студента: "))
                fio = input("Введите ФИО: ")
                spec = input("Введите специальность: ")
                faculty.enroll_student(sid, fio, spec)
                print("Студент зачислен")

            elif choice == "2":
                sid = int(input("Введите ID студента для отчисления: "))
                faculty.expel_student(sid)
                print("Студент отчислен")

            elif choice == "3":
                sid = int(input("Введите ID студента: "))
                student = faculty.find_student(sid)
                if student:
                    student_menu(faculty, student)
                else:
                    print("Студент с таким ID не найден")

            elif choice == "4":
                name = input("Введите название дисциплины: ")
                d = faculty.find_discipline(name)
                if d:
                    path = save_discipline_report(faculty, d)
                    print(f"Ведомость по дисциплине сохранена: {path}")
                else:
                    print("Дисциплина не найдена")

            elif choice == "0":
                print("Выход")
                break
            else:
                print("Неверный ввод")

        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()