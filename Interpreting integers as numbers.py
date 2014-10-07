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

if year == 1:
    year_full = 2001
elif year == 2:
    year_full = 2002
elif year == 3:
    year_full = 2003
elif year == 4:
    year_full = 2004
elif year == 5:
    year_full = 2005
elif year == 6:
    year_full = 2006
elif year == 7:
    year_full = 2007
elif year == 8:
    year_full = 2008
elif year == 9:
    year_full = 2009
elif year == 10:
    year_full = 2010
elif year == 11:
    year_full = 2011
elif year == 12:
    year_full = 2012
elif year == 13:
    year_full = 2013
elif year == 14:
    year_full = 2014
else:
    year_full = "ERROR"
    
print("The date is the {0}{1} of {2} {3}.".format(day, day_suffix, month_name, year_full))
