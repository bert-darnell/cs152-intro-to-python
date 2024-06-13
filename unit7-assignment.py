# Bert Darnell
# 4/29/2021
#
# This program writes a file with the total crime rate for a state in a year
# this function writes my dictionaries
def to_dict(key, value):
    crime_summary = {}
    crime_summary[key] = value
    return crime_summary

# this function writes to a new file
def write_to(year_dict, crime_dict, wfile):
    #this block separates my nested dictionaries
    for key in year_dict:
        crime_dictionary = year_dict[key]
        #this block writes the state, total crime, and year
        for k, v in crime_dictionary.items():
            wfile.write(k.ljust(25))
            wfile.write(v.ljust(25))
            wfile.write(key)
            wfile.write('\n')

# this block opens the .csv file to read, and creates a new write file
with open('state_crime - CS152.csv', 'r') as file:
    wfile = open('crime_summary.txt', 'w')
    # this block writes my header in new .txt file
    wfile.write('State'.ljust(25))
    wfile.write('Reported Crimes'.ljust(25))
    wfile.write('Year\n')
    
    # this block iterates through my .csv file
    aline = file.readline()
    for aline in file:
        aline = aline.split(',')
        # this block totals the crime per state in year
        total_crime = 0
        total_crime = int(aline[11]) + int(aline[15])
        total_crime = '{:,}'.format(total_crime)
        
        #this block calls my functions to create the dictionaries
        crime_summary = to_dict(aline[10], total_crime)
        year_crime_summary = to_dict(aline[20], crime_summary)
        write_to(year_crime_summary, crime_summary, wfile)
    
    #closes write .txt file
    wfile.close()
