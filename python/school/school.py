
# Cody Leeper aka CodyCodes
# CSC200 2020
# School Transcripts Project

# Run and enter main() to start program

# Algorithm


### THIS IS SOMETHING I WANT ####
#! TODO: George Smith ID 222333 Summer 2019
#! CSC 200 - Introduction to Computer Science - 3 credit hours - Grade A
#! CSC 201 - Computer Science I - 4 credit hours - Grade B
#! gpa: 3.43

#? A is 4 B 3 c 2 d 1 f or i is 0 
#gpa is cl sumal course pnts * course cedit / total credit 

class Student:
    # init attr of student name id and year
    def __init__(self, name = '', studentId = '', semester = '', semesterYear = ''):
        self.name = name
        self.studentId = studentId
        self.semester = semester
        self.semesterYear = semesterYear
        self.gpa = float(0)

    def __str__(self):
        return 'Student Nanme:' + self.name + ' ID:' + self.studentId + ' Semester:' + self.semester + ' Year:' + self.semesterYear

    def getGPA(self):
        return self.gpa

    def setGPA(self, gpa):
        # 0 !less gpa !greater 4.0
        self.gpa = gpa
        if self.gpa <= 4.0 and self.gpa > 0.0:
            return self.gpa
        else:
            self.gpa = 0
            return 'GPA Not Excepted'

#? A=4 B=3 C=2 D=1 F or I =0 
#gpa is cl sumal course pnts * course cedit / total credit 

class Course:

    # init attr of coursename coursenumber and grade
    def __init__(self, courseNumber='', courseName='',creditHours=''):
        self.courseName = courseName
        self.courseNumber = courseNumber
        self.creditHours = creditHours
        self.grade = 'I'

    def __str__(self):
        return self.courseNumber + '-' + self.courseName + '-' + self.creditHours

    def getCreditHours(self,creditHours):
        return self.creditHours
    
    def setGrade(self, grade):
        if grade in ('A','B', 'C', 'D', 'E','F','I'):
            self.grade = grade
            return self.grade
        else:
            self.grade = 'I'
            return self.grade

    def getGrade(self):
        return self.grade
    
    def getPoints(self):
        if self.grade == 'A':
            return 4
        elif self.grade == 'B':
            return 3
        elif self.grade == 'C':
            return 2
        elif self.grade == 'D':
            return 1
        elif self.grade == 'F':
            return 0
        elif self.grade == 'I':
            return 0
        else:
            return 'Invalid input'

def main():
    programIntroduction()

    # NewStudent Region

    name = input('Enter student name:')
    studentId = input('Enter student ID:')
    semester = input('Enter student attended semester:')
    semesterYear = input('Enter student semester year:')

    # Create a student object with specific student information
    newStudent = Student(name, studentId, semester, semesterYear)

    # Test function for Student Object
    testStudentFunction(newStudent)
    # END REGION

    # Courses Region

    # 1. Create a course number with information for a specific course
    courseNumber = input('Enter course number:')
    courseName = input('Enter course name:')
    creditHours = input('Enter course number:')
    # 2. Call the print function to verify that your __str__ method is working correctly
    newCourse = Course(courseNumber, courseName, creditHours)
   # Test function for Course Object
    testCourseFunction(newCourse, creditHours)
    # END Region

def programIntroduction():
    print('Welcome to the School Transcripts Program\n')
    print('Enter a make model and year of your choice.')



def testStudentFunction(newStudent):
    # 2. Call the print function and to verify that your __str__ function is working correctly
    print(f'{newStudent}')
    # # 3. Call the setGPA() function and pass it a valid gpa value
    testStudentGPAPass = newStudent.setGPA(4)
    # # 4. Call the getGPA() function and print the return value
    print(f'GPA Paas: {testStudentGPAPass}')
    # # 5. Call the setGPA() function and pass it an invalid gpa value
    testStudentGPAFail = newStudent.setGPA(5)
    # # 6. Verify that error message appears
    print(f'GPA Fail: {testStudentGPAFail}')
    # # 7. Call the getGPA() function and print the return value to verify that it is set to 0
    returnvalGPA = newStudent.getGPA()
    print(f'Return val GPA: {returnvalGPA}')

def testCourseFunction(newCourse, creditHours):
     # 3. Call the getCreditHours method and verify that the credit hours variable is set correctly
    testCreditHours = newCourse.getCreditHours(creditHours)
    # 4. Call the setGrade method and pass it a valid letter grade
    testSetGradePass = newCourse.setGrade("A")
    print(f'GradePass: {testSetGradePass}')
    # 5. Call the getPoints() method and verify that the correct point value is returned
    testgetPointsvalreturn = newCourse.getPoints()
    print(f'Points: {testgetPointsvalreturn}')
    # 6. Call the setGrade method again and pass it an invalid letter grade
    testSetGradeFail = newCourse.setGrade("G")
    # 7. Verify that the error message appears
    print(f'GradeFail: {testSetGradeFail}')
    # 8. Call getGrade and verify that the grade has been set to ‘I’
    testGetGrade = newCourse.getGrade()
    print(f'GradeClear: {testGetGrade}')
    # 9. Call getPoints and verify that the point value is 0
    returnValGetPoints = newCourse.getPoints()
    print(f'Points:{returnValGetPoints}')

if __name__ == '__main__':
    main()