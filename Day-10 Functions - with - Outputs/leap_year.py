def is_leap_year(year):
    if (year % 4 == 0 and (year % 100 != 0)) or year % 400 == 0:
        return True
    else:
        return False
    
year_list = [2000,2020,2024,2400,1700,1989,2100]

for year in year_list:
    print(is_leap_year(year))
