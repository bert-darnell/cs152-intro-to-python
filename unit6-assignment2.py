
def print_format(aline):
    line = aline.strip('\n')
    values = line.split(',')
    print(values[2].ljust(20), values[0].ljust(15), values[3].ljust(10), values[5].ljust(5))
    
def number_total(aline):
    line = aline.strip('\n')
    values = aline.split(',')
    number = int(values[3])
    return number

def table(file):
    location_check = input('Enter a location ').upper()
    disease_check = input('Enter a disease ').upper()
    year_check = input('Enter a year ')
    
    print('State'.ljust(20), 'Disease'.ljust(15), 'Number'.ljust(10), 'Year\n'.ljust(5))
    
    total_number = 0
    for aline in file:
        if location_check in aline:
            if disease_check in aline:
                if year_check in aline:
                    print_format(aline)
                    total_number += number_total(aline)
                                

    print('Total: '.rjust(30), str(total_number).rjust(10))


file = open("health-no-head.csv", "r")
table(file)
file.close()

# Question 5 Answers:
# 1) How many cases of Hepatitis A were reported in Utah in 2001? 59
# 2) How many cases of polio have been reported in California? 47,743
# 3) How many cases of all diseases were reported in 1956? 633,753
