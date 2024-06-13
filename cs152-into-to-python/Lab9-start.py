def filtered(aline):
    line = aline.strip('\n')
    values = line.split(',')
    print(values[2].ljust(20), values[0].ljust(15), values[3].ljust(10), values[5].ljust(5))
    
def num_total(aline):
    line = aline.strip('\n')
    values = aline.split(',')
    number = int(values[3])
    return number


def check_table(file):
    location_check = input('Enter a location ').upper()
    disease_check = input('Enter a disease ').upper()
    year_check = input('Enter a year ').upper()
    
    total_number = 0
    for aline in file:
        if location_check in aline:
            if disease_check in aline:
                if year_check in aline:
                    filtered(aline)
                    total_number += num_total(aline)

            else:
                if year_check in aline:
                    filtered(aline)
                    total_number += num_total(aline)
        elif disease_check in aline:
            if year_check in aline:
                filtered(aline)
                total_number += num_total(aline)
    
    print('Total:        '.rjust(35), total_number)


file = open("health-no-head-sample.csv", "r")
check_table(file)
file.close()

