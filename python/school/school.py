
# Cody Leeper aka CodyCodes
# CSC200 2020
# School Transcripts Project

# Run and enter main() to start program

# Algorithm
#
### THIS IS SOMETHING I WANT ####
# George Smith ID 222333 Summer 2019
# CSC 200 - Introduction to Computer Science - 3 credit hours - Grade A
# CSC 201 - Computer Science I - 4 credit hours - Grade B
# GPA: 3.43

class Student:
    # init attr of student name id and year
    def __init__(self, name = '', studentId = '', semesterYear = ''):
        self.name = name
        self.studentId = studentId
        self.semesterYear = semesterYear
        self.gpa = 0

    def __str__(self):
        return 'Student Nanme:' + self.name + ' ID:' + self.studentId + ' Semester:' + self.semesterYear

    def setGPA(gpa):
        return gpa

    def getGPA(self):
        return self.gpa

class Course:
    # init attr of coursename coursenumber and grade
    def __init__(self, courseName, courseNumber, grade):
        self.courseName = courseName
        self.courseNumber = courseNumber
        self.grade = grade

def main():
    programIntroduction()

    name = input('Enter student name:')
    studentId = input('Enter student ID:')
    semesterYear = input('Enter student semester year:')

    newStudent = Student(name, studentId, semesterYear)

    print(f'{newStudent}')


def programIntroduction():
    print('Welcome to the School Transcripts Program\n')
    print('Enter a make model and year of your choice.')

if __name__ == '__main__':
    main()
