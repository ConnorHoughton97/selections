# Connor Houghton
# 07.10.2014
# Interpreting integers as dates.

day = int(input("Please enter the day in numbers: "))
month = int(input("Please enter the month in numbers: "))
year = int(input("please enter the last two digits of the year: "))


if day == 1 or day == 21 or day == 31:
    day_suffix = "st"
elif day == 2 or day == 22:
    day_suffix = "nd"
elif day == 3 or day == 23:
    day_suffix = "rd"
elif 4 <= day <= 20 or 24 <= day <= 30: 
    day_suffix = "th"
else:
    day_suffix = "ERROR"
    

if month == 1:
    month_name = "January"
elif month == 2:
    month_name = "Febuary"
elif month == 3:
    month_name = "March"
elif month == 4:
    month_name = "April"
elif month == 5:
    month_name = "May"
elif month == 6:
    month_name = "June"
elif month == 7:
    month_name = "July"
elif month == 8:
    month_name = "August"
elif month == 9:
    month_name = "September"
elif month == 10:
    month_name = "October"
elif month == 11:
    month_name = "November"
elif month == 12:
    month_name = "December"
else:
    month_name = "ERROR"

if 31 <= year <= 99:
    year_first_two_digits = 19
elif 0 <= year <= 30:
    year_first_two_digits = 20

if 0 <= year <= 9:    
    print("The date is the {0}{1} of {2} {3}0{4}.".format(day, day_suffix, month_name, year_first_two_digits, year))
else:
    print("The date is the {0}{1} of {2} {3}{4}.".format(day, day_suffix, month_name, year_first_two_digits, year))
