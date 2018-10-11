#This program computes how old my family members are in a given year.

def college(Kidname, Age):
    if Age > 17 and Age < 22:
        print(Kidname + ' will be in college')

for year in range(2018,2040):
    People = ['Ed', 'Teresa', 'Christian', 'Genevieve']
    BirthYear = [1981, 1986, 2014, 2018]
    print('In the year ' + str(year))
    for i in range(len(People)):
        print(People[i] + ' will be ' + str(year - BirthYear[i]) + \
              ' years of age.')
        college(People[i], (year-BirthYear[i]))
#    print('Ed will be ' + str(year - 1981) + ' years of age.')
#    print('Teresa will be ' + str(year - 1986) + ' years of age.')
#    Cage = year - 2014
#    Gage = year - 2018
#    print('Christian will be ' + str(Cage) + ' years of age.')
#    print('Genevieve will be ' + str(Gage) + ' years of age.')
#    college('Christian', Cage)
#    college('Genevieve', Gage)
