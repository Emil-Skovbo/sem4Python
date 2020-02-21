import random


class Student():
    def __init__(self, name, gender, dataSheet, image_url):
        self.name = name
        self.gender = gender
        self.dataSheet = dataSheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.dataSheet, self.image_url)

    def get_avg_grade(self):
        avg = sum(self.dataSheet.get_grades_as_list) / \
            len(self.dataSheet.get_grades_as_list)
        return avg


class DataSheet():
    def __init__(self, course=[]):
        self.course = course

    def get_grades_as_list(self, course=1):
        return list(self.course.grade)


class Course():
    def __init__(self, name, classroom, teacher, etcs, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade

    def __repr__(self):
        return 'Course(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.etcs, self.grade)


def randomStudent(n):
    listofpersons = []
    name = ["alpha", "benny", "cell", "denis", "emil", "freddrik"]
    gender = ["male", "female", "apache attack helicopter"]
    grade = ["-3", "00", "02", "4", "7", "10", "12"]
    course1 = Course("datamat", "103", "lam", "noget",
                     grade[random.randint(0, len(grade)-1)])
    course2 = Course("computerscience", "203", "lammer", "noget",
                     grade[random.randint(0, len(grade)-1)])
    ds = DataSheet([course1, course2])
    imageurl = ["https://external-preview.redd.it/TyZq1U0HS16W_0DKSr6atvTqVJ1KgZn8K-S3DMvNz_A.jpg?auto=webp&s=b044116323b40fe7f32affd3868098e18f1e2125", "https://preview.redd.it/oq5e3cc3p8g41.png?width=640&height=703&crop=smart&auto=webp&s=166f7c0cbcd5988eaaac74efbc1c06ae6b89c5f4",
                "https://preview.redd.it/0nhjao9asag41.jpg?width=960&crop=smart&auto=webp&s=c266179ac7999205f89a1ba69819d27cb94ab204", "https://preview.redd.it/tl89zdzwcag41.jpg?width=640&height=896&crop=smart&auto=webp&s=964a1b4a83cbcfa31bd0084d9ff88002776c5a30"]
    for i in range(0, n):
        person = Student(name[random.randint(0, len(name)-1)],
                         gender[random.randint(0, len(gender)-1)],
                         ds.course[random.randint(0, len(ds.course)-1)],
                         imageurl[random.randint(0, len(imageurl)-1)])
        listofpersons.append(person)
    return listofpersons


print(randomStudent(3))
