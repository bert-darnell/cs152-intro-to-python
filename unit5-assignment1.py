# Bert Darnell
# 4/18/2021
#
# This program is answering questions from cs152 unit 5 assignment 
#
# It takes the poorly entered data and seperates course numbers, course title, and enrollment

#this table prints the course number and seperates the number for a abreviation
def table1(courses):
    print(' -------\n', 'Table 1\n','-------')
    for acourse in courses:
        print (acourse[0:2],acourse[2:5])
    return ''

# this table seperates the enrolment number
def table2(courses):
     print(' -------\n', 'Table 2\n','-------')
     for acourse in courses:
        #this splits the enrolment 
        course_strip = acourse.strip('1234567890')
        x = len(course_strip)
        print(acourse[0:2], acourse[2:5], course_strip, acourse[x:])
     return ''

# this table cuts the name of class short, lines up enrolment and totals it.
def table3(courses):
    print(' -------\n', 'Table 3\n','-------')
    total_enroll = 0
    for acourse in courses:
        course_strip = acourse.strip('1234567890')
        x = len(course_strip)
        #sets the length for enrolment number
        enrollment = acourse[x:]
        total_enroll = total_enroll + int(enrollment)
        print(acourse[0:2], acourse[2:5], course_strip[5:25].ljust(20),
              enrollment.rjust(3))
    print('Total:'.rjust(27), total_enroll)
    return ''
    
#this table assigns the length of table, according to the length of the class titles
def table4(courses):
    long = max(len(acourse) for acourse in courses)
    print(' -------\n', 'Table 4\n','-------')
    courses.sort()
    for acourse in courses:
        course_strip = acourse.strip('1234567890')
        ### sets the enrolment length to come after the course title
        x = len(course_strip)
        enrollment = acourse[x:]
        print(acourse[0:2], acourse[2:5], course_strip[5:].ljust(long), enrollment.rjust(3))
    return ''
def main():
    ### Data entry for course number, class name, and enrolment number
    courses = ['CS152Introduction to Python Programming21',
               'CS369Operating Systems Administration8',
               'CS352Data Structures19',
               'CS208Discrete Mathematics124',
               'CS319Computer Architecture14',
               'MA221Calculus and Analytical Geometry for Majors I12',
               'MA311Linear Algebra7',
               'MA150Precalculus Mathematics27',
               'CS335Introduction to Cybersecurity20',
               'IS361Data Management Systems22',
               'MG315Advanced Business Statistics6',
               'XX999I Made This Class Up23',
               'ZZ123Class of the champions 101B23']
               
            
    ### input to select which table to view     
    table_select = input("What table would you like to see? 1,2,3, or 4:")
    if table_select == '1':
        print(table1(courses))
    elif table_select == '2':
        print(table2(courses))
    elif table_select == '3':
        print(table3(courses))
    else:
        print(table4(courses))

main()
