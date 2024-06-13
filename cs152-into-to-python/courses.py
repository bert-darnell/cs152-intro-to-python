# Given a list strings containing
#   department code, course number, course title, enrollment
# Print a series of tables in different formats
# Unfortunately, the spacing between each of these items was lost when
# each string was generated. You will have to deal with this in your program. 
#  

def main():
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
               'MG315Advanced Business Statistics6' ]
               
            
    # Print the table without formatting
    for aCourse in courses:      
        print(aCourse)

main()
